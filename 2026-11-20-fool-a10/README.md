# Fool, Ascension 10, 20 new seeds (2026-11-20)

**13 wins, 7 losses.** The full write-up, with setup, seed selection, and per-run results, is in [docs/results.md](https://github.com/langwhat/slay-the-spire-2-harness/blob/1598a67592bc770c9623baa08e3c04bdda0d4b8b/docs/results.md) in the harness repository, fixed at the revision that reports this batch. The [latest version](https://github.com/langwhat/slay-the-spire-2-harness/blob/main/docs/results.md) may carry later corrections.

See [How the seeds were chosen](https://github.com/langwhat/slay-the-spire-2-harness/blob/1598a67592bc770c9623baa08e3c04bdda0d4b8b/docs/results.md#how-the-seeds-were-chosen)
for the seed generator, the local timestamps, and the steps to spot-check a run in the game.

## Runs

"Seed as played" is the seed the game used after mapping `I`→`1` and `O`→`0`. The result file is the one that counts for each run.

| Run | Seed as played | Result | Files |
| --- | --- | --- | --- |
| 01 | `C0DXV1SEH0BM` | Win | [01-control-02/](01-control-02/) · [`result.json`](01-control-02/result.json) |
| 02 | `T3ZX6GPYQ3CW` | Win | [02-control-02/](02-control-02/) · [`result.json`](02-control-02/result.json) |
| 03 | `RRQZ7NFVF7FU` | Win | [03-control-02/](03-control-02/) · [`result.json`](03-control-02/result.json) |
| 04 | `DW7EWVRDDPTP` | Win | [04-control-02/](04-control-02/) · [`result.json`](04-control-02/result.json) |
| 05 | `LPHEHMCQTC36` | Win | [05-control-01/](05-control-01/) · [`result.json`](05-control-01/result.json) |
| 06 | `Z7VVLHWKQZKJ` | Win | [06-control-01/](06-control-01/) · [`result.json`](06-control-01/result.json) |
| 07 | `R4D4F3G1DC18` | Win | [07-control-01/](07-control-01/) · [`verified-result.json`](07-control-01/verified-result.json) |
| 08 | `RUBX2060M76S` | Win | [08-control-01/](08-control-01/) · [`verified-result.json`](08-control-01/verified-result.json) |
| 09 | `ZDR8ZQEFVVDG` | Loss | [09-control-01/](09-control-01/) · [`result.json`](09-control-01/result.json) |
| 10 | `EFASQD0T11H5` | Loss | [10-control-01/](10-control-01/) · [`verified-result.json`](10-control-01/verified-result.json) |
| 11 | `PUQMC1CYQQN1` | Loss | [11-control-01/](11-control-01/) · [`verified-result.json`](11-control-01/verified-result.json) |
| 12 | `CTVG3HF5QTBR` | Loss | [12-control-01/](12-control-01/) · [`result.json`](12-control-01/result.json) |
| 13 | `DV7H9SP8CJDV` | Win | [13-control-01/](13-control-01/) · [`result.json`](13-control-01/result.json) |
| 14 | `FZZLWLEZU1VB` | Win | [14-control-01/](14-control-01/) · [`result.json`](14-control-01/result.json) |
| 15 | `1XSSMSMYHKEG` | Loss | [15-control-01/](15-control-01/) · [`result.json`](15-control-01/result.json) |
| 16 | `LKDHCMWUWT2G` | Loss | [16-control-01/](16-control-01/) · [`result.json`](16-control-01/result.json) |
| 17 | `0LMHJT09JU1C` | Win | [17-control-01/](17-control-01/) · [`result.json`](17-control-01/result.json) |
| 18 | `QUVTKD0V1PCR` | Win | [18-control-01/](18-control-01/) · [`result.json`](18-control-01/result.json) |
| 19 | `F1MQ1ZAK2F4G` | Win | [19-control-01/](19-control-01/) · [`result.json`](19-control-01/result.json) |
| 20 | `D7KJBUG0VHR8` | Loss | [20-control-01/](20-control-01/) · [`result.json`](20-control-01/result.json) |

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
