import hashlib
from pathlib import Path

from . import paths
from .util import load_yaml


def published() -> dict:
    return load_yaml(paths.journal() / "checks" / "versions.yaml")


def machine_sha() -> str:
    """Hash of the check code itself, so a finding names the exact implementation that produced it."""
    h = hashlib.sha256()
    package = Path(__file__).parent
    for file in sorted(package.rglob("*.py")):
        h.update(file.relative_to(package).as_posix().encode() + b"\0")
        h.update(file.read_bytes().replace(b"\r\n", b"\n"))
    return h.hexdigest()[:12]
