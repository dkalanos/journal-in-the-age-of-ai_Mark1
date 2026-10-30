from .base import Check, Context, NotRun
from . import anchors, completeness, form, injection, resolution
from ..sieve import contribution, perturbation, soundness

# run order: the injection screen goes last so it can read what the models reported along the way
REGISTRY: tuple[Check, ...] = (
    form.CHECK,
    completeness.CHECK,
    resolution.CHECK,
    anchors.CHECK,
    contribution.CHECK,
    soundness.CHECK,
    perturbation.CHECK,
    injection.CHECK,
)

__all__ = ["Check", "Context", "NotRun", "REGISTRY"]
