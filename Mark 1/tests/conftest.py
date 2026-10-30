import json
import shutil
from pathlib import Path

import pytest
import yaml

from machine import generator
from machine.record import Record

ROOT = Path(__file__).resolve().parents[1]
ANSWERS = Path(__file__).parent / "answers"
PAPER = "questions-before-priors"
DEFAULT_ANSWERS = {
    "generate": "generate.json",
    "completeness": "completeness.json",
    "resolution": "resolution.json",
    "contribution": "contribution-none.json",
}


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    """A private copy of the journal (with its corpus) and Questions Before Priors; MARK1_ROOT points the code at it.

    The copy has the one Level 1 finding of the record's first run corrected (claim C10's evidence pointer named a
    function, not lines), so that the tests start from a record the deterministic checks find clean.
    """
    shutil.copytree(ROOT / "1-journal", tmp_path / "1-journal")
    record = tmp_path / "2-author" / PAPER
    shutil.copytree(ROOT / "2-author" / PAPER, record,
                    ignore=shutil.ignore_patterns("self-check", "submission.yaml", "*.rtf", "__pycache__"))
    claims = record / "ai-appendix" / "claims.yaml"
    claims.write_text(claims.read_text(encoding="utf-8").replace("materials/lab.py:repairs", "materials/lab.py:L81-L90"),
                      encoding="utf-8")
    generator.restamp(Record.load(record))
    venues = tmp_path / "1-journal" / "corpus" / "venues.yaml"
    # tests never reach the network: the hand list alone, which is what the canned answers cite
    cfg = yaml.safe_load(venues.read_text(encoding="utf-8"))
    cfg.update(search=[], hand_list=True)
    venues.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")
    monkeypatch.setenv("MARK1_ROOT", str(tmp_path))
    return tmp_path


def answer(run_folder: Path, **overrides: str) -> int:
    """Fill every waiting bundle of a run with a canned payload, as an answering model would."""
    files = {**DEFAULT_ANSWERS, **overrides}
    filled = 0
    for request_file in sorted(run_folder.glob("bundles/*/request.json")):
        request = json.loads(request_file.read_text(encoding="utf-8"))
        payload = json.loads((ANSWERS / files[request["check"]]).read_text(encoding="utf-8"))
        for k in sorted(request_file.parent.glob("k*")):
            if (k / "response.json").exists():
                continue
            envelope = {"nonce": request["nonce"], "check": request["check"], "check_version": request["check_version"],
                        "model": "canned", "model_version": "test", "answered_by": "pytest",
                        "injection_observed": [], "payload": payload}
            (k / "response.json").write_text(json.dumps(envelope), encoding="utf-8")
            filled += 1
    return filled
