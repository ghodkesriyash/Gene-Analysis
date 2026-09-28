"""Scan raw DNA samples for disease-associated repeats and save a results CSV.

Usage:
    python src/analyze.py --input data/Raw_Data1.txt --output data/results.csv
"""
import argparse

import numpy as np
import pandas as pd

from config import DISEASES, RAW_DATA_PATH, RESULTS_CSV_PATH
from detector import is_pathogenic, max_consecutive_repeats


def load_samples(path) -> pd.DataFrame:
    with open(path) as f:
        sequences = f.read().split()
    return pd.DataFrame({"Serial_No": range(1, len(sequences) + 1),
                         "DNA_Sample": sequences})


def analyze(df: pd.DataFrame) -> pd.DataFrame:
    for code, d in DISEASES.items():
        counts = df["DNA_Sample"].map(lambda s: max_consecutive_repeats(s, d["motif"]))
        hit = counts.map(lambda c: is_pathogenic(c, d["min_repeats"], d["max_repeats"]))
        df[d["label"]] = np.where(hit, "Found", "Not Found")
        df[f"{code}_repetitions"] = counts.where(hit, np.nan)
    return df


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=str(RAW_DATA_PATH))
    parser.add_argument("--output", default=str(RESULTS_CSV_PATH))
    args = parser.parse_args()

    df = analyze(load_samples(args.input))
    df.to_csv(args.output, index=False)
    print(f"Analysed {len(df)} samples -> {args.output}")
    for code, d in DISEASES.items():
        print(f"  {d['label']:<30} {int((df[d['label']] == 'Found').sum()):>5}")


if __name__ == "__main__":
    main()
