# All-6-character rotation, Ascension 10, 36 runs (`v0.114.0`, 2026-11-26 to 2026-11-27)

**21 wins, 15 losses (58.3%), best streak 9 wins.** Full write-up, token usage, timing, and technical notes are in [docs/results.md](https://github.com/langwhat/slay-the-spire-2-harness/blob/main/docs/results.md) in the harness repository.

- **Game:** Slay the Spire 2 `v0.114.0` (`a7b9a9c0`, Windows, Standard, Ascension 10)
- **Mode:** Standalone core in minimal mode (`STS2_MINIMAL=true`), no external knowledge base, no viewer input
- **Model:** `gpt-6.2-astra` (Responses protocol, reasoning effort `xhigh`)
- **Core revisions:** `44cd9b1` for Runs 12–36 (25 runs: 13 wins, 12 losses); Runs 01–11 (11 runs: 8 wins, 3 losses) ran across earlier ancestors on the same branch during live updates (`16f4447`, `3291601`, `52f2244`, `df68e80`, `4302239`, `80312b7`)

## Runs

| # | Character | Seed | Result | Floor | Core | Files |
| --- | --- | --- | --- | ---: | --- | --- |
| 01 | Ironclad | `CSWSC29RD8F6` | Loss | 33 | `16f4447` | [01-ironclad/](01-ironclad/) · [`archive.sqlite`](01-ironclad/archive.sqlite) · [`eval-source.json`](01-ironclad/eval-source.json) · [`1795677399.run`](01-ironclad/1795677399.run) |
| 02 | Silent | `G7PXZV3VGUC0` | Win | 49 | `16f4447` | [02-silent/](02-silent/) · [`archive.sqlite`](02-silent/archive.sqlite) · [`eval-source.json`](02-silent/eval-source.json) · [`1795679805.run`](02-silent/1795679805.run) |
| 03 | Regent | `021C3Z3A1880` | Win | 49 | `3291601` | [03-regent/](03-regent/) · [`archive.sqlite`](03-regent/archive.sqlite) · [`eval-source.json`](03-regent/eval-source.json) · [`1795683219.run`](03-regent/1795683219.run) |
| 04 | Necrobinder | `GGMSN6P0G6W1` | Win | 49 | `52f2244` | [04-necrobinder/](04-necrobinder/) · [`archive.sqlite`](04-necrobinder/archive.sqlite) · [`eval-source.json`](04-necrobinder/eval-source.json) · [`1795687582.run`](04-necrobinder/1795687582.run) |
| 05 | Defect | `6RYMUBWKVY6F` | Win | 49 | `52f2244` | [05-defect/](05-defect/) · [`archive.sqlite`](05-defect/archive.sqlite) · [`eval-source.json`](05-defect/eval-source.json) · [`1795691245.run`](05-defect/1795691245.run) |
| 06 | Fool | `M17QSY8K2SDX` | Loss | 48 | `52f2244` | [06-fool/](06-fool/) · [`part1-archive.sqlite`](06-fool/part1-archive.sqlite) · [`part2-archive.sqlite`](06-fool/part2-archive.sqlite) · [`1795694838.run`](06-fool/1795694838.run) |
| 07 | Ironclad | `6AJXKED2SGB1` | Win | 49 | `df68e80` | [07-ironclad/](07-ironclad/) · [`archive.sqlite`](07-ironclad/archive.sqlite) · [`eval-source.json`](07-ironclad/eval-source.json) · [`1795698157.run`](07-ironclad/1795698157.run) |
| 08 | Silent | `NXZJDJWVP5QE` | Loss | 48 | `4302239` | [08-silent/](08-silent/) · [`archive.sqlite`](08-silent/archive.sqlite) · [`eval-source.json`](08-silent/eval-source.json) · [`1795702167.run`](08-silent/1795702167.run) |
| 09 | Regent | `HS2JULYVMEG1` | Win | 49 | `4302239` | [09-regent/](09-regent/) · [`archive.sqlite`](09-regent/archive.sqlite) · [`eval-source.json`](09-regent/eval-source.json) · [`1795705181.run`](09-regent/1795705181.run) |
| 10 | Necrobinder | `QN3PMXA654MP` | Win | 49 | `4302239` | [10-necrobinder/](10-necrobinder/) · [`archive.sqlite`](10-necrobinder/archive.sqlite) · [`eval-source.json`](10-necrobinder/eval-source.json) · [`1795708171.run`](10-necrobinder/1795708171.run) |
| 11 | Defect | `YG8A4U2Q4NNS` | Win | 49 | `80312b7` | [11-defect/](11-defect/) · [`archive.sqlite`](11-defect/archive.sqlite) · [`eval-source.json`](11-defect/eval-source.json) · [`1795711893.run`](11-defect/1795711893.run) |
| 12 | Fool | `DQPRV7NG001J` | Loss | 49 | `44cd9b1` | [12-fool/](12-fool/) · [`archive.sqlite`](12-fool/archive.sqlite) · [`eval-source.json`](12-fool/eval-source.json) · [`1795714657.run`](12-fool/1795714657.run) |
| 13 | Ironclad | `R7X5E4YC3THJ` | Loss | 49 | `44cd9b1` | [13-ironclad/](13-ironclad/) · [`archive.sqlite`](13-ironclad/archive.sqlite) · [`eval-source.json`](13-ironclad/eval-source.json) · [`1795717194.run`](13-ironclad/1795717194.run) |
| 14 | Silent | `LZY086GL2EY8` | Loss | 49 | `44cd9b1` | [14-silent/](14-silent/) · [`archive.sqlite`](14-silent/archive.sqlite) · [`eval-source.json`](14-silent/eval-source.json) · [`1795719590.run`](14-silent/1795719590.run) |
| 15 | Regent | `LBAJVWWL7RMR` | Loss | 49 | `44cd9b1` | [15-regent/](15-regent/) · [`archive.sqlite`](15-regent/archive.sqlite) · [`eval-source.json`](15-regent/eval-source.json) · [`1795722452.run`](15-regent/1795722452.run) |
| 16 | Necrobinder | `0XWS2DXRE9PA` | Loss | 27 | `44cd9b1` | [16-necrobinder/](16-necrobinder/) · [`archive.sqlite`](16-necrobinder/archive.sqlite) · [`eval-source.json`](16-necrobinder/eval-source.json) · [`1795724926.run`](16-necrobinder/1795724926.run) |
| 17 | Defect | `0XPJ29PP8VZW` | Loss | 49 | `44cd9b1` | [17-defect/](17-defect/) · [`archive.sqlite`](17-defect/archive.sqlite) · [`eval-source.json`](17-defect/eval-source.json) · [`1795726258.run`](17-defect/1795726258.run) |
| 18 | Fool | `DMRBC6B42UUH` | Loss | 48 | `44cd9b1` | [18-fool/](18-fool/) · [`archive.sqlite`](18-fool/archive.sqlite) · [`eval-source.json`](18-fool/eval-source.json) · [`1795729160.run`](18-fool/1795729160.run) |
| 19 | Ironclad | `6UKXMSG3B59U` | Loss | 49 | `44cd9b1` | [19-ironclad/](19-ironclad/) · [`archive.sqlite`](19-ironclad/archive.sqlite) · [`eval-source.json`](19-ironclad/eval-source.json) · [`1795731537.run`](19-ironclad/1795731537.run) |
| 20 | Silent | `6C38MZWE5Q3A` | Win | 49 | `44cd9b1` | [20-silent/](20-silent/) · [`archive.sqlite`](20-silent/archive.sqlite) · [`eval-source.json`](20-silent/eval-source.json) · [`1795734207.run`](20-silent/1795734207.run) |
| 21 | Regent | `L8ACM2N3EGYE` | Loss | 48 | `44cd9b1` | [21-regent/](21-regent/) · [`archive.sqlite`](21-regent/archive.sqlite) · [`eval-source.json`](21-regent/eval-source.json) · [`1795737355.run`](21-regent/1795737355.run) |
| 22 | Necrobinder | `1RJRMNDYPPYD` | Win | 49 | `44cd9b1` | [22-necrobinder/](22-necrobinder/) · [`archive.sqlite`](22-necrobinder/archive.sqlite) · [`eval-source.json`](22-necrobinder/eval-source.json) · [`1795740377.run`](22-necrobinder/1795740377.run) |
| 23 | Defect | `99BRCD6NC1ZY` | Win | 49 | `44cd9b1` | [23-defect/](23-defect/) · [`archive.sqlite`](23-defect/archive.sqlite) · [`eval-source.json`](23-defect/eval-source.json) · [`1795743283.run`](23-defect/1795743283.run) |
| 24 | Fool | `84QFWS3C2JZ7` | Loss | 17 | `44cd9b1` | [24-fool/](24-fool/) · [`archive.sqlite`](24-fool/archive.sqlite) · [`eval-source.json`](24-fool/eval-source.json) · [`1795745972.run`](24-fool/1795745972.run) |
| 25 | Ironclad | `MSK69DD6QTMU` | Win | 49 | `44cd9b1` | [25-ironclad/](25-ironclad/) · [`archive.sqlite`](25-ironclad/archive.sqlite) · [`eval-source.json`](25-ironclad/eval-source.json) · [`1795746902.run`](25-ironclad/1795746902.run) |
| 26 | Silent | `DREWDRD62GFQ` | Win | 49 | `44cd9b1` | [26-silent/](26-silent/) · [`archive.sqlite`](26-silent/archive.sqlite) · [`eval-source.json`](26-silent/eval-source.json) · [`1795749759.run`](26-silent/1795749759.run) |
| 27 | Regent | `0XENTSUP0PF4` | Win | 49 | `44cd9b1` | [27-regent/](27-regent/) · [`archive.sqlite`](27-regent/archive.sqlite) · [`eval-source.json`](27-regent/eval-source.json) · [`1795753851.run`](27-regent/1795753851.run) |
| 28 | Necrobinder | `UU1T5RCMHDHN` | Win | 49 | `44cd9b1` | [28-necrobinder/](28-necrobinder/) · [`archive.sqlite`](28-necrobinder/archive.sqlite) · [`eval-source.json`](28-necrobinder/eval-source.json) · [`1795757262.run`](28-necrobinder/1795757262.run) |
| 29 | Defect | `FN5TECMQG55D` | Win | 49 | `44cd9b1` | [29-defect/](29-defect/) · [`archive.sqlite`](29-defect/archive.sqlite) · [`eval-source.json`](29-defect/eval-source.json) · [`1795760669.run`](29-defect/1795760669.run) |
| 30 | Fool | `RMHUDHW9035F` | Win | 49 | `44cd9b1` | [30-fool/](30-fool/) · [`archive.sqlite`](30-fool/archive.sqlite) · [`eval-source.json`](30-fool/eval-source.json) · [`1795764824.run`](30-fool/1795764824.run) |
| 31 | Ironclad | `VNGYNPV5CHT6` | Win | 49 | `44cd9b1` | [31-ironclad/](31-ironclad/) · [`archive.sqlite`](31-ironclad/archive.sqlite) · [`eval-source.json`](31-ironclad/eval-source.json) · [`1795768179.run`](31-ironclad/1795768179.run) |
| 32 | Silent | `73WL95FHY5F4` | Win | 49 | `44cd9b1` | [32-silent/](32-silent/) · [`archive.sqlite`](32-silent/archive.sqlite) · [`eval-source.json`](32-silent/eval-source.json) · [`1795771341.run`](32-silent/1795771341.run) |
| 33 | Regent | `0NZWMJMEWM3Q` | Win | 49 | `44cd9b1` | [33-regent/](33-regent/) · [`archive.sqlite`](33-regent/archive.sqlite) · [`eval-source.json`](33-regent/eval-source.json) · [`1795775095.run`](33-regent/1795775095.run) |
| 34 | Necrobinder | `5QZ98LW8H2XJ` | Loss | 33 | `44cd9b1` | [34-necrobinder/](34-necrobinder/) · [`archive.sqlite`](34-necrobinder/archive.sqlite) · [`eval-source.json`](34-necrobinder/eval-source.json) · [`1795778271.run`](34-necrobinder/1795778271.run) |
| 35 | Defect | `027AG9NV7MMH` | Win | 49 | `44cd9b1` | [35-defect/](35-defect/) · [`archive.sqlite`](35-defect/archive.sqlite) · [`eval-source.json`](35-defect/eval-source.json) · [`1795780145.run`](35-defect/1795780145.run) |
| 36 | Fool | `1K3J6638M3N6` | Loss | 49 | `44cd9b1` | [36-fool/](36-fool/) · [`archive.sqlite`](36-fool/archive.sqlite) · [`eval-source.json`](36-fool/eval-source.json) · [`1795783370.run`](36-fool/1795783370.run) |

## Directory contents

| File | Contents |
| --- | --- |
| `archive.sqlite` (or `part1-archive.sqlite` + `part2-archive.sqlite` for Run 06) | The core's SQLite archive (schema 22) recording every game operation, model request, usage count, and viewer reason. |
| `eval-source.json` | Recorded core revision, game version/commit, character, and seed. |
| `<timestamp>.run` | The game's own native run history JSON from `saves/history/`. |

## Inspecting an archive

```sh
uv run sts2 journal --archive 01-ironclad/archive.sqlite
```

## Notes

- Run 06 (`06-fool`, seed `M17QSY8K2SDX`) experienced one mid-run backend reconnect at `node-39`, producing two sequential archive files (`part1-archive.sqlite` and `part2-archive.sqlite`) for the same game instance (`cf44acc2a51d4b7e8e6201bfb48cac3b:run-1`). The game itself was not restarted or reloaded.
- SQLite archives contain full prompts, model outputs, and OpenAI encrypted reasoning items; no API credentials, `.env` files, or local machine logs are included.
