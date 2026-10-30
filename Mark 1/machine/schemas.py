from functools import cache
from pathlib import Path
from urllib.parse import urljoin

from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

from . import paths
from .util import load_yaml

BASE = "https://mark1.local/schemas/"


class SchemaError(ValueError):
    def __init__(self, name: str, errors: list[str]):
        self.name, self.errors = name, errors
        super().__init__(f"{name}: " + "; ".join(errors[:3]))


@cache
def _registry(folder: Path) -> Registry:
    resources = []
    for file in sorted(folder.glob("*.schema.yaml")):
        contents = {**load_yaml(file), "$id": BASE + file.name}
        resources.append((BASE + file.name, Resource.from_contents(contents, default_specification=DRAFT202012)))
    return Registry().with_resources(resources)


def _folder() -> Path:
    return paths.journal() / "protocol" / "schemas"


def schema(name: str) -> dict:
    return _registry(_folder()).contents(f"{BASE}{name}.schema.yaml")


def errors(name: str, data) -> list[str]:
    validator = Draft202012Validator(schema(name), registry=_registry(_folder()))
    found = sorted(validator.iter_errors(data), key=lambda e: [str(p) for p in e.absolute_path])
    return [f"{'/'.join(map(str, e.absolute_path)) or '(root)'}: {e.message}" for e in found]


def validate(name: str, data) -> None:
    if problems := errors(name, data):
        raise SchemaError(name, problems)


def expanded(name: str) -> dict:
    """The schema with every $ref inlined, for showing to whoever answers a prompt."""
    registry = _registry(_folder())

    def walk(node, base: str):
        if isinstance(node, list):
            return [walk(v, base) for v in node]
        if not isinstance(node, dict):
            return node
        if "$ref" in node:
            uri, _, fragment = urljoin(base, node["$ref"]).partition("#")
            target = registry.contents(uri)
            for part in filter(None, fragment.split("/")):
                target = target[part]
            return walk(target, uri)
        return {k: walk(v, base) for k, v in node.items() if k not in ("$id", "$defs")}

    return walk(schema(name), f"{BASE}{name}.schema.yaml")
