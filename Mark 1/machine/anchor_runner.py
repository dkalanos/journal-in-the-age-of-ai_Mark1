"""Re-executes one reproduction anchor in a fresh interpreter. JSON spec on stdin, JSON result on stdout."""
import importlib.util
import json
import sys
from pathlib import Path


def main() -> None:
    spec = json.load(sys.stdin)
    sys.path.insert(0, spec["package_parent"])
    import sympy
    from machine import sym

    try:
        names = sym.symbols(spec.get("symbols") or {name: {} for name in spec.get("params") or {}})
        if "points" in spec:  # perturbation: the same procedure at many parameter values, in one interpreter
            print(json.dumps({"ok": True, "values": [value_at({**spec, "params": point}, names, sym, sympy)
                                                     for point in spec["points"]]}))
            return
        value = compute(spec, names, sym, sympy)
        print(json.dumps(compare(spec, value, names, sym, sympy)))
    except Exception as e:
        print(json.dumps({"ok": False, "error": f"{type(e).__name__}: {e}"}))


def value_at(spec: dict, names: dict, sym, sympy) -> dict:
    try:
        return {"value": str(sympy.sympify(compute(spec, names, sym, sympy)))}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


MODULES = {}


def compute(spec: dict, names: dict, sym, sympy):
    procedure, params = spec["procedure"], spec.get("params") or {}
    if procedure["language"] == "python":
        file, _, func = procedure["source"].partition(":")
        if file not in MODULES:
            module_spec = importlib.util.spec_from_file_location("procedure", Path(spec["record_root"]) / file)
            MODULES[file] = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(MODULES[file])
        return getattr(MODULES[file], func)(**params)
    expr = sym.parse(procedure["source"], names)
    return expr.subs({names[k]: sympy.nsimplify(v, rational=True) for k, v in params.items() if k in names})


def compare(spec: dict, value, names: dict, sym, sympy) -> dict:
    kind, expected = spec["kind"], spec["expected"]
    result = sympy.sympify(value)
    if kind == "numeric":
        tolerance = spec.get("tolerance") or {}
        allowed = max(tolerance.get("abs", 1e-9), tolerance.get("rel", 0) * abs(float(expected)))
        return {"ok": True, "value": str(result), "passed": abs(float(result) - float(expected)) <= allowed}
    if kind == "sign":
        sign = ("zero" if result.is_zero else "positive" if result.is_positive
                else "negative" if result.is_negative else "undetermined")
        return {"ok": True, "value": str(result), "sign": sign, "passed": sign == expected}
    return {"ok": True, "value": str(result), "passed": sym.equal(result, sym.parse(str(expected), names))}


if __name__ == "__main__":
    main()
