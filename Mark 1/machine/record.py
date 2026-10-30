from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .util import load_yaml, sha256_files

AI_APPENDIX_FILES = ("definitions.md", "procedure.md", "claims.yaml", "stance.md", "anchors.yaml", "scope.md")
HASHED_PARTS = ("record.yaml", "declarations.yaml", "paper", "appendix", "ai-appendix", "materials", "provenance")
# generator bundles sit under provenance/ but they are run artifacts, not part of the record
SKIPPED_DIRS = {"generation", "__pycache__"}


@dataclass
class Record:
    root: Path
    ai_dir: Path

    @classmethod
    def load(cls, root: Path, ai_dir: Path | None = None) -> "Record":
        root = Path(root)
        return cls(root=root, ai_dir=Path(ai_dir) if ai_dir else root / "ai-appendix")

    @property
    def manifest(self) -> dict:
        return self._mapping("record.yaml")

    @property
    def paper_id(self) -> str:
        return self.manifest.get("paper_id", self.root.name)

    @property
    def declarations(self) -> dict:
        return self._mapping("declarations.yaml")

    @property
    def claims(self) -> list[dict]:
        return self._entries("ai-appendix/claims.yaml", "claims")

    @property
    def anchors(self) -> list[dict]:
        return self._entries("ai-appendix/anchors.yaml", "anchors")

    @property
    def derivations(self) -> list[dict]:
        return self._entries("provenance/derivations.yaml", "derivations")

    def claim(self, claim_id: str | None) -> dict | None:
        return next((c for c in self.claims if c.get("id") == claim_id), None)

    def derivation(self, derivation_id: str | None) -> dict | None:
        return next((d for d in self.derivations if d.get("id") == derivation_id), None)

    def is_main(self, claim_id: str | None) -> bool:
        return bool((self.claim(claim_id) or {}).get("main"))

    def path(self, rel: str) -> Path:
        head, _, rest = rel.partition("/")
        if head == "ai-appendix":
            return self.ai_dir / rest if rest else self.ai_dir
        return self.root / rel

    def exists(self, rel: str) -> bool:
        return self.path(rel).exists()

    def text(self, rel: str) -> str:
        return self.path(rel).read_text(encoding="utf-8")

    def table(self, rel: str) -> Any:
        path = self.path(rel)
        return load_yaml(path) if path.is_file() else None

    def files(self, rel_dir: str) -> list[str]:
        base = self.path(rel_dir)
        if base.is_file():
            return [rel_dir]
        if not base.is_dir():
            return []
        prefix = rel_dir.rstrip("/")
        return sorted(
            f"{prefix}/{p.relative_to(base).as_posix()}"
            for p in base.rglob("*")
            if p.is_file() and not SKIPPED_DIRS & set(p.relative_to(base).parts)
        )

    def has_ai_appendix(self) -> bool:
        return any((self.ai_dir / name).exists() for name in AI_APPENDIX_FILES)

    def sha(self) -> str:
        return sha256_files((rel, self.path(rel)) for part in HASHED_PARTS for rel in self.files(part))

    def _mapping(self, rel: str) -> dict:
        try:
            data = self.table(rel)
        except Exception:
            return {}
        return data if isinstance(data, dict) else {}

    def _entries(self, rel: str, key: str) -> list[dict]:
        entries = self._mapping(rel).get(key)
        return [e for e in entries if isinstance(e, dict)] if isinstance(entries, list) else []
