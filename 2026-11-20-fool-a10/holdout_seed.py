"""Match the native v0.113.1 seed alphabet used by SeedHelper.CanonicalizeSeed."""


def canonical_seed(seed: str) -> str:
    return seed.upper().replace("O", "0").replace("I", "1").strip()
