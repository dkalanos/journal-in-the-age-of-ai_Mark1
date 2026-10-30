"""M2 · The modality router: which checks apply to the declared kind of research (appendix D.4).
Applying hypothesis-testing standards to interpretive work would itself be a warrant error."""
from dataclasses import dataclass

from .record import Record


class NotBuilt(Exception):
    pass


@dataclass(frozen=True)
class Modality:
    name: str
    protocol: str
    checks: tuple[str, ...]


BUILT = {
    "formal": Modality("formal", "protocol/formal.md",
                       ("form", "completeness", "resolution", "anchors", "contribution", "soundness", "perturbation",
                        "injection")),
}
SPECIFIED = ("empirical", "simulation", "qualitative", "verbal", "survey")


def route(record: Record) -> Modality:
    name = record.declarations.get("modality") or record.manifest.get("modality")
    if name in BUILT:
        return BUILT[name]
    if name in SPECIFIED:
        raise NotBuilt(f"the {name} modality is specified in journal/protocol/modalities.md; its checks are Stage 2")
    raise NotBuilt(f"the record declares no known modality ({name!r})")
