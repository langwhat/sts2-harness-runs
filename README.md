# sts2-harness runs

Recorded full runs of [slay-the-spire-2-harness](https://github.com/langwhat/slay-the-spire-2-harness), kept as evidence for its published results.

| Batch | Setup | Result |
| --- | --- | --- |
| [2026-11-20-fool-a10](2026-11-20-fool-a10/) | Fool, Ascension 10, 20 new seeds; core `f0486a9`, `gpt-6.2-astra` (`xhigh`), knowledge `bdf5079` | 13 wins, 7 losses |

Each run directory holds the core's SQLite archive, which records every game operation and model request, plus logs and the game's own saves and run history. Inspect an archive with the core revision that recorded it:

```sh
uv run sts2 journal --archive <run>/instance/archive.sqlite
```

## License

[MIT](LICENSE).
