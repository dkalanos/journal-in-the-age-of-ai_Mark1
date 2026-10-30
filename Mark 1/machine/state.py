"""Where a paper stands, derived by replaying its review history. Every human step checks it first."""
from dataclasses import dataclass

from . import history

AFTER_DECISION = {
    "proceed_to_review": "awaiting_new",
    "return_for_corrections": "returned_for_corrections",
    "return_without_review": "returned",
    "refer_to_specialist": "referred",
}
NEXT = {
    "draft": "the author runs `mark1 check <paper>`, then `mark1 submit <paper>`",
    "submitted": "the journal runs `mark1 check <paper> --actor journal`",
    "checked": "a named editor runs `mark1 intake <paper> <run-id> --signed-by NAME`",
    "referred": "the named specialist runs `mark1 intake <paper> <run-id> --signed-by SPECIALIST`",
    "returned_for_corrections": "the author corrects the record, re-runs the checks, and resubmits",
    "returned": "nothing further; a new submission is new work",
    "awaiting_new": "the author answers the map once (`mark1 answer`), then an editor signs `mark1 new`; or the "
                    "editor defers \"new\" to a later round (`mark1 defer-new`) and review proceeds",
    "in_review": "`mark1 packet`, reviewer reports (`mark1 report`), then `mark1 interest`, or `mark1 revise`",
    "revise_requested": "the author revises the record, re-runs the checks, and resubmits; the journal re-runs its "
                        "checks and an editor decides intake again, against the same review history",
    "awaiting_certificate": "the editor runs `mark1 issue <paper> --by EDITOR`",
    "closed": "nothing further; the negative outcome produces no public object",
    "certified": "nothing further; the certificate and publication are issued",
}


class StateError(RuntimeError):
    pass


@dataclass
class State:
    name: str = "draft"
    round: int = 0
    last_run: str | None = None
    passes_used: int = 0
    answered: bool = False
    new_deferred: bool = False
    new_signed: bool = False
    specialist: str | None = None

    @property
    def next(self) -> str:
        return NEXT[self.name]


def state(paper_id: str) -> State:
    s = State()
    for e in history.events(paper_id):
        match e["event"]:
            case "submitted":
                s.round = e["round"]
                # a revision is a new submission against the same review history: checked, then intake (Fig. 4, A5)
                s.name = "in_review" if s.name == "in_review" else "submitted"
            case "checked":
                s.last_run = e["run_id"]
                s.name = "checked" if s.name == "submitted" else s.name
            case "decided":
                s.name = AFTER_DECISION[e["action"]]
                if s.name == "awaiting_new" and s.new_signed:
                    s.name = "in_review"  # "new" is signed once per paper; a later round proceeds straight to review
                s.specialist = e.get("specialist")
                s.passes_used += e["action"] == "return_for_corrections"
            case "answered":
                s.answered = True
            case "new_deferred":
                s.name, s.new_deferred = "in_review", True
            case "new_signed":
                s.name = "in_review" if e["new"] else "returned"
                s.new_deferred, s.new_signed = False, e["new"]
            case "revise_requested":
                s.name = "revise_requested"
            case "interest_signed":
                s.name = "awaiting_certificate" if e["interesting"] else "closed"
            case "issued":
                s.name = "certified"
    return s


def require(paper_id: str, *allowed: str) -> State:
    s = state(paper_id)
    if s.name not in allowed:
        wanted = " or ".join(a.replace("_", " ") for a in allowed)
        raise StateError(f"{paper_id} is {s.name.replace('_', ' ')}; this step needs it to be {wanted}. Next: {s.next}")
    return s
