"""Play one declared holdout seed and record its native terminal outcome."""

import argparse
import json
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path

from sts2_knowledge.entry import entry_materials

from holdout_seed import canonical_seed
from sts2_harness.cli import main as harness_main
from sts2_harness.client import models as native
from sts2_harness.journal import Journal

OUT = Path(__file__).resolve().parent
GAME = OUT / "game/SlayTheSpire2.app/Contents/MacOS/Slay the Spire 2"
TEMPLATE = OUT.parent / "STS2-fool-A10-astra-8headless/template/native.manifest.json"
ENV = OUT.parent.parent / "2026-11-17/STS2-growth-high-54/connection.env"
OVERRIDES = {
    "LLM_MODEL": "gpt-6.2-astra",
    "LLM_PROTOCOL": "responses",
    "LLM_REASONING_EFFORT": "xhigh",
    "LLM_CONTEXT_WINDOW": "300000",
    "LLM_SERVICE_TIER": "default",
}


def read_terminal(archive: Path, declared_seed: str) -> dict[str, object]:
    seed = canonical_seed(declared_seed)
    with closing(Journal.open(archive)) as journal:
        if journal.manifest.seed != seed:
            raise RuntimeError("Observed seed differs from the declared holdout.")
        headless = journal.manifest.headless
        if headless is None or headless.start_receipt.seed != seed:
            raise RuntimeError("The completed seed receipt differs from the declared holdout.")
        for record in reversed(journal.operations(attempts=False)):
            if record.reply is None:
                continue
            terminal = next(
                (obs.state for obs in reversed(record.reply.observations)
                 if isinstance(obs.state, native.TerminalState)),
                None,
            )
            if terminal is not None:
                return {"canonical_seed": seed, "native_result": terminal.result.value,
                        "terminal_hp": terminal.player.hp, "terminal_floor": terminal.progress.floor}
    return {"canonical_seed": seed}


def main(arm: str, index: int, attempt: int) -> None:
    seeds = json.loads((OUT / "protocol.json").read_text())["holdout"]["seeds"]
    seed = seeds[index - 1]
    root = OUT / "holdout" / f"{index:02}-{arm}-{attempt:02}"
    root.mkdir(parents=True)
    instance = root / "instance"
    started = datetime.now(UTC).isoformat()
    result: dict[str, object] = {
        "arm": arm,
        "index": index,
        "seed": seed,
        "attempt": attempt,
        "started": started,
    }
    try:
        arguments = [
            "headless",
            "--env-file",
            str(ENV),
            "--game",
            str(GAME),
            "--template",
            str(TEMPLATE),
            "--character",
            "FOOL",
            "--ascension",
            "10",
            "--seed",
            seed,
            "--instance",
            str(instance),
            "--output",
            str(root / "runs"),
        ]
        for key, value in {
            **OVERRIDES,
            "STS2_DRIVER": "builtin",
            "STS2_USER_INPUT": "false",
            "STS2_MINIMAL": "false",
        }.items():
            arguments.extend(("--set", f"{key}={value}"))
        result["exit"] = harness_main(arguments, materials=entry_materials())
        if (archive := instance / "archive.sqlite").exists():
            result.update(read_terminal(archive, seed))
        result["state"] = (
            "terminal" if result.get("native_result") in {"victory", "defeat"} else "incomplete"
        )
    except Exception as exc:
        result.update(state="error", error=f"{type(exc).__name__}: {exc}")
        raise
    finally:
        result["ended"] = datetime.now(UTC).isoformat()
        temporary = root / "result.tmp"
        temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        temporary.replace(root / "result.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("arm", choices=["control", "candidate"])
    parser.add_argument("index", type=int, choices=range(1, 21))
    parser.add_argument("--attempt", type=int, default=1)
    args = parser.parse_args()
    main(args.arm, args.index, args.attempt)
