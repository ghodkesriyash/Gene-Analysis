"""Generate synthetic DNA samples with disease-associated repeat insertions.

Usage:
    python src/generate_data.py --n 4000 --seed 42
"""
import argparse
import random

from config import RAW_DATA_PATH

SAMPLE_LENGTH = 3000

# disease -> (repeat motif, threshold repeats)
DISEASE_MOTIFS = {
    "HD": ("CAG", 36),
    "FXS": ("CGG", 200),
    "DM1": ("CTG", 50),
    "DPA": ("CAG", 40),
    "FD": ("GGGGCC", 30),
    "SCA8": ("CAG", 70),
    "SCA4": ("CAG", 40),
    "FA": ("GAA", 66),
    "FXTAS": ("CGG", 55),
    "OPMD": ("GCG", 8),
}


def make_sample(choices):
    disease = random.choice(choices)
    if disease is None:
        return "".join(random.choices("ACTG", k=SAMPLE_LENGTH))
    motif, threshold = DISEASE_MOTIFS[disease]
    repeat_count = random.randint(threshold, threshold + 50)
    disease_seq = motif * repeat_count
    remaining = SAMPLE_LENGTH - len(disease_seq)
    background = "".join(random.choices("ACTG", k=remaining))
    pos = random.randint(0, remaining)
    return background[:pos] + disease_seq + background[pos:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=4000, help="number of samples")
    parser.add_argument("--seed", type=int, default=None, help="random seed")
    parser.add_argument("--out", default=str(RAW_DATA_PATH), help="output file")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    names = list(DISEASE_MOTIFS)
    choices = names * 10 + [None] * len(names)  # ~10:1 diseased : healthy

    with open(args.out, "w") as f:
        for _ in range(args.n):
            f.write(make_sample(choices) + "\n")
    print(f"Wrote {args.n} samples to {args.out}")


if __name__ == "__main__":
    main()
