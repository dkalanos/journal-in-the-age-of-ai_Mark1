import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

RUNNER = Path(__file__).with_name("anchor_runner.py")
PACKAGE_PARENT = Path(__file__).resolve().parents[1]


def run_isolated(spec: dict, timeout: float = 10) -> dict:
    # Fresh interpreter, empty temp cwd, scrubbed env, hard timeout. That isolates crashes and hangs;
    # it is not a jail (Windows gives us no cheap network or filesystem sandbox). machine/README.md says so.
    # -B: no bytecode is written beside the record's materials.
    env = {k: v for k, v in os.environ.items() if k.upper() in ("SYSTEMROOT", "WINDIR")}
    payload = json.dumps({**spec, "package_parent": str(PACKAGE_PARENT)})
    with tempfile.TemporaryDirectory() as tmp:
        try:
            proc = subprocess.run([sys.executable, "-I", "-B", str(RUNNER)], input=payload, capture_output=True,
                                  text=True, timeout=timeout, cwd=tmp, env=env)
        except subprocess.TimeoutExpired:
            return {"ok": False, "error": f"timed out after {timeout:g}s"}
    if proc.returncode != 0:
        tail = proc.stderr.strip().splitlines()
        return {"ok": False, "error": tail[-1] if tail else f"exited with code {proc.returncode}"}
    return json.loads(proc.stdout)
