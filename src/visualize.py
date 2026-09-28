"""Create the heatmap, pie chart and bar graph from the results CSV.

Usage:
    python src/visualize.py --input data/results.csv
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from config import DISEASES, FIG_DIR, RESULTS_CSV_PATH


def disease_counts(df: pd.DataFrame):
    labels = [d["label"] for d in DISEASES.values()]
    counts = [int((df[l] == "Found").sum()) for l in labels]
    return labels, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=str(RESULTS_CSV_PATH))
    parser.add_argument("--outdir", default=str(FIG_DIR))
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    labels, counts = disease_counts(df)
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    # 1. Heatmap
    plt.figure(figsize=(12, 4))
    sns.heatmap(pd.DataFrame([counts], columns=labels), cmap="coolwarm", cbar=True)
    plt.title("Disease Counts Heatmap")
    plt.yticks([])
    plt.tight_layout()
    plt.savefig(out / "heatmap.png", dpi=150)
    plt.close()

    # 2. Pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Distribution of Detected Diseases")
    plt.tight_layout()
    plt.savefig(out / "pie_chart.png", dpi=150)
    plt.close()

    # 3. Bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(labels, counts, color="lightgreen")
    plt.xlabel("Disease Name")
    plt.ylabel("Number of Cases")
    plt.title("Counts of Detected Repeat-Based Diseases")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out / "bar_graph.png", dpi=150)
    plt.close()

    print(f"Saved figures to {out}")


if __name__ == "__main__":
    main()
