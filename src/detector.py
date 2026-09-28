"""Core motif-repeat detection logic."""
import re


def max_consecutive_repeats(sequence: str, motif: str) -> int:
    """Return the longest run of back-to-back `motif` copies in `sequence`.

    Equivalent to the original `check()` scan in the notebook (left-to-right,
    non-overlapping, count resets on a mismatch) but implemented with a
    regex so it is much faster on 3000-base samples.
    """
    runs = re.finditer(f"(?:{motif})+", sequence)
    return max((len(m.group()) // len(motif) for m in runs), default=0)


def is_pathogenic(count: int, min_repeats: int, max_repeats=None) -> bool:
    """True if the repeat count falls inside the disease range."""
    if count < min_repeats:
        return False
    return max_repeats is None or count <= max_repeats
