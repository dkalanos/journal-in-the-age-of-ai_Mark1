"""Departure statistics (appendix F.4): how often each editor departs from the standard action, and which way."""
import csv
from collections import defaultdict
from pathlib import Path

from . import history, paths
from .util import write_text

CAVEAT = ("The rate shows how editors behave relative to the published mapping. It cannot show whether the "
          "mapping is good: a mapping that returns everything shows zero departures.")


def departures() -> tuple[Path, Path]:
    rows: dict[str, dict] = defaultdict(lambda: {"decisions": 0, "departures": 0, "stricter": 0, "more_lenient": 0})
    signed: dict[str, dict] = defaultdict(lambda: {"signatures": 0, "departures": 0})
    for log in sorted(paths.editor().glob("*/history.jsonl")):
        for e in history.events(log.parent.name):
            if e["event"] == "new_signed":
                signed[e["signed_by"]]["signatures"] += 1
                signed[e["signed_by"]]["departures"] += bool(e.get("departure"))
            if e["event"] != "decided":
                continue
            row = rows[e["signed_by"]]
            row["decisions"] += 1
            if departure := e.get("departure"):
                row["departures"] += 1
                row[departure["direction"]] += 1
    out = paths.editor() / "statistics"
    out.mkdir(parents=True, exist_ok=True)
    fields = ["editor", "decisions", "departures", "rate", "stricter", "more_lenient"]
    table = [{"editor": name, **r, "rate": round(r["departures"] / r["decisions"], 3)} for name, r in sorted(rows.items())]
    with (out / "departures.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(table)
    lines = ["# Departures from the standard action", "", CAVEAT, "",
             "| Editor | Decisions | Departures | Rate | Stricter | More lenient |", "|---|---|---|---|---|---|"]
    lines += [f"| {r['editor']} | {r['decisions']} | {r['departures']} | {r['rate']:.0%} | {r['stricter']} | "
              f"{r['more_lenient']} |" for r in table] or ["| _no decisions yet_ | | | | | |"]
    lines += ["", "## Departures from the map at \"new\"", "",
              "The map proposes the kind on the question as the paper states it. An editor who signs another kind, or "
              "reads the question otherwise, records why; this counts those signatures.", "",
              "| Editor | Signatures | Departures from the map |", "|---|---|---|"]
    lines += [f"| {name} | {r['signatures']} | {r['departures']} |" for name, r in sorted(signed.items())] \
        or ["| _nothing signed yet_ | | |"]
    write_text(out / "departures.md", "\n".join(lines) + "\n", rtf=True)
    return out / "departures.md", out / "departures.csv"
