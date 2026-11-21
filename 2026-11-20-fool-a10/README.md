# Fool, Ascension 10, 20 new seeds (2026-11-20)

**13 wins, 7 losses.** The full write-up, with setup, seed selection, and per-run results, is in [docs/results.md](https://github.com/langwhat/slay-the-spire-2-harness/blob/main/docs/results.md) in the harness repository.

## Setup

- **Game:** Slay the Spire 2 v0.113.1 (macOS), Standard mode, Fool, Ascension 10.
- **Code:** core `f0486a9` with `paired-eval.patch`, an evaluation-only change later committed as `be09282`. Knowledge `sts2-knowledge` at `bdf5079`.
- **Model:** `gpt-6.2-astra`, Responses, effort `xhigh`, service tier `default`, context window 300,000.
- **Mode:** ordinary mode, builtin driver, launched with `sts2 headless`, one instance per run.

## Files

| Path | Contents |
| --- | --- |
| `protocol.json` | The plan frozen before any run: the 20 seeds, the arms, and the known inputs. |
| `data-freeze.json` | SHA-256 of the protocol, patch, launch scripts, and installed `sts2agent.dll` at freeze time. |
| `seed-normalization-amendment.json` | Record of the seed readback correction (the game maps `I`→`1` and `O`→`0`), with script hashes. It was written before any outcome was inspected. |
| `run_full.py`, `holdout_seed.py`, `recover_holdout_seed.py` | The launch script, the seed normalization, and the readback for runs whose first check failed on seed spelling. |
| `paired-eval.patch` | The evaluation patch applied on top of `f0486a9`. |
| `NN-control-AA/` | One run: seed index `NN`, launch attempt `AA`. |

Inside each run directory:

| Path | Contents |
| --- | --- |
| `result.json` | Seed, start and end times, native result, final floor and HP. |
| `verified-result.json` | Runs 07, 08, 10, 11 only: the result after the seed readback correction. The original `result.json` is kept. |
| `instance/archive.sqlite` | The core's archive of every game operation, model request, and material read. |
| `instance/diagnostics.jsonl`, `bootstrap.jsonl`, `status.json`, `game.*.log` | Backend diagnostics, startup evidence, final status, and game output. |
| `instance/initial-observation.json` | The paused game state before Start. |
| `instance/appdata/` | The game's own saves, run history (`saves/history/*.run`), replay, and Godot log. |

## Recording provenance

Absolute paths in the logs and status files point into the batch directory on
the original machine. They retain their recorded values to match the SQLite
archives.

[`run_full.py`](run_full.py) launched the recorded runs and matches the hash in
the seed normalization amendment. It imports `sts2_knowledge` and references a
native start template and a `connection.env` file from other local batches.
Those batch directories and configuration files are outside this repository.
Credentials were supplied separately through the environment file.

The SQLite archives contain full prompts, model outputs, knowledge document
bodies, and OpenAI's encrypted reasoning items.

## Not included

- Game resources staged from the installation (`instance/engine/`).
- Copies of the native start template (`runs/templates/`). The archive manifest records the template digest.
- The game's telemetry identifier (`sentry.dat`).
- The per-instance user-data alias (`instance/home/`).

Runs 01–04 are attempt `02` because their first launches exited during Python import, before the game started or any model request was sent.
