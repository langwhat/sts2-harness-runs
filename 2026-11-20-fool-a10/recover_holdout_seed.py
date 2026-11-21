"""Confirm an already finished trial after an exact native seed normalization mismatch."""

import argparse
import json

from holdout_seed import canonical_seed
from run_full import OUT, read_terminal


def recover(label: str):
    index_text, arm, attempt_text = label.split("-")
    index, attempt = int(index_text), int(attempt_text)
    assert 1 <= index <= 20 and attempt >= 1 and arm in {"control", "candidate"}
    assert label == f"{index:02}-{arm}-{attempt:02}"
    root = OUT / "holdout" / label
    previous = json.loads((root / "result.json").read_text())
    seed = json.loads((OUT / "protocol.json").read_text())["holdout"]["seeds"][index - 1]
    assert seed == previous["seed"] and canonical_seed(seed) != seed
    assert previous["exit"] == 0 and previous["state"] == "error"
    assert previous["error"] == "RuntimeError: Observed seed differs from the declared holdout."
    instance = root / "instance"
    start = json.loads((instance / "start.json.result.json").read_text())
    assert start["status"] == "completed" and start["effect_verified"]
    assert start["seed"] == canonical_seed(seed)
    terminal = read_terminal(instance / "archive.sqlite", seed)
    assert terminal.get("native_result") in {"victory", "defeat"}
    (history,) = (instance / "appdata").glob("**/history/*.run")
    native = json.loads(history.read_text())
    assert native["seed"] == canonical_seed(seed) and native["ascension"] == 10
    assert native["players"][0]["character"] == "CHARACTER.FOOL"
    assert not native.get("was_abandoned") and not native.get("is_custom_game")
    assert terminal["native_result"] == ("victory" if native["win"] else "defeat")
    repaired = previous | terminal | {"state": "terminal", "earlier_seed_check_error": previous["error"]}
    repaired.pop("error")
    with (root / "verified-result.json").open("x") as stream:
        stream.write(json.dumps(repaired, ensure_ascii=False, indent=2) + "\n")
    print(label, "sealed after native seed and terminal corroboration", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("label", nargs="+")
    for label in parser.parse_args().label:
        recover(label)
