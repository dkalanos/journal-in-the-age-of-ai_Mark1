from collections import Counter
from collections.abc import Hashable, Iterable
from itertools import combinations

from ..pointer import Span


def jaccard(a: set, b: set) -> float:
    return 1.0 if not a and not b else len(a & b) / len(a | b)


def mean_pairwise_jaccard(sets: list[set]) -> float:
    pairs = list(combinations(sets, 2))
    return sum(jaccard(x, y) for x, y in pairs) / len(pairs) if pairs else 1.0


def quorum_items(sets: Iterable[set], quorum: int) -> set:
    counts = Counter(item for s in sets for item in s)
    return {item for item, n in counts.items() if n >= quorum}


def quorum_value(values: list[Hashable], quorum: int) -> Hashable | None:
    if not values:
        return None
    value, n = Counter(values).most_common(1)[0]
    return value if n >= quorum else None


def cluster_spans(runs: list[list[tuple[Span, str]]], quorum: int) -> tuple[list[list[tuple[int, Span, str]]], float]:
    """Group overlapping spans across runs. Two runs rarely cite identical line ranges for the same
    statement, so overlap in the same file counts as agreement. Returns the clusters a quorum of runs
    found, and the share of all clusters that reached quorum."""
    items = [(i, span, text) for i, run in enumerate(runs) for span, text in run]
    parent = list(range(len(items)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in combinations(range(len(items)), 2):
        if items[a][1].overlaps(items[b][1]):
            parent[find(a)] = find(b)
    groups: dict[int, list] = {}
    for idx, item in enumerate(items):
        groups.setdefault(find(idx), []).append(item)
    clusters = list(groups.values())
    agreed = [c for c in clusters if len({i for i, _, _ in c}) >= quorum]
    return agreed, (len(agreed) / len(clusters) if clusters else 1.0)
