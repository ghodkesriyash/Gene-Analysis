"""Shared configuration: disease motifs, thresholds and file paths."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "docs" / "figures"

RAW_DATA_PATH = DATA_DIR / "Raw_Data1.txt"
RESULTS_CSV_PATH = DATA_DIR / "results.csv"

# code -> disease label, repeat motif, pathogenic repeat range.
# Thresholds match the original notebook (PROJECT.ipynb).
DISEASES = {
    "HD":   dict(label="Huntington's_Disease",         motif="CAG",    min_repeats=36,  max_repeats=None),
    "FXS":  dict(label="Fragile_x_syndrome",           motif="CGG",    min_repeats=200, max_repeats=None),
    "MD":   dict(label="Myotonic_dystrophy",           motif="CTG",    min_repeats=50,  max_repeats=None),
    "DPA":  dict(label="Dentatorubral-PA",             motif="CAG",    min_repeats=40,  max_repeats=None),
    "FA":   dict(label="Friedreichs_Ataxia",           motif="GAA",    min_repeats=66,  max_repeats=None),
    "AS":   dict(label="Ataxia_Syndrome",              motif="CGG",    min_repeats=55,  max_repeats=None),
    "OPMD": dict(label="OPMD",                         motif="GGC",    min_repeats=8,   max_repeats=None),
    "SA8":  dict(label="Spinocerebellar_Ataxia_Type8", motif="CAG",    min_repeats=70,  max_repeats=None),
    "SA4":  dict(label="Spinocerebellar_Ataxia_Type4", motif="CAG",    min_repeats=40,  max_repeats=80),
    "FD":   dict(label="Frontotemporal_Dementia",      motif="GGGGCC", min_repeats=30,  max_repeats=None),
}
