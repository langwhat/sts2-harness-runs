# sts2-harness runs

Recorded full runs of [slay-the-spire-2-harness](https://github.com/langwhat/slay-the-spire-2-harness), kept as open-source evidence for published results across game versions.

| Batch | Game version | Setup | Result |
| --- | --- | --- | --- |
| [2026-11-26-rotation-a10](2026-11-26-rotation-a10/) | `v0.114.0` | All 6 characters rotation (6 runs each), Ascension 10; standalone core (`44cd9b1` for Runs 12–36; see batch README), minimal mode, no external knowledge base, `gpt-6.2-astra` (`xhigh`) | 21 wins, 15 losses (best streak 9) |
| [2026-11-20-fool-a10](2026-11-20-fool-a10/) | `v0.113.1` | Fool, Ascension 10, 20 new seeds; core `f0486a9`, `gpt-6.2-astra` (`xhigh`), knowledge `bdf5079` *(archived; retired from main README due to newly-seen Boss ordering in the save template)* | 13 wins, 7 losses |

Each run directory holds the core's SQLite archive (which records every game operation and model request), provenance metadata, and the game's own `.run` history. Inspect an archive with the matching core revision:

```sh
uv run sts2 journal --archive <run>/archive.sqlite
```

## Disclaimer

This is an unofficial fan project, not affiliated with or endorsed by Mega Crit. Slay the Spire is a trademark of Mega Crit. The run records include saves, replays, and run histories that the game produced during these runs; this repository contains no game code or assets.

## License

[MIT](LICENSE).
