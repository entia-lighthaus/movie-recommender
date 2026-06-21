"""
Step 1: Look at the data.

No models, no predictions — just to confirm what we're actually working
with..
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")   

train = pd.read_csv(DATA_DIR / "train.csv")
test  = pd.read_csv(DATA_DIR / "test.csv")

print("=" * 60) 
print("TRAIN.CSV")
print("=" * 60)
print(train.head())
print(f"\nShape: {train.shape}")
print(f"Columns: {list(train.columns)}")
print(f"\nRating min/max: {train['rating'].min()} / {train['rating'].max()}")
print(f"Unique users : {train['userId'].nunique():,}")
print(f"Unique movies: {train['movieId'].nunique():,}")
print(f"\nAny missing values?\n{train.isnull().sum()}")

print("\n" + "=" * 60)
print("TEST.CSV")
print("=" * 60)
print(test.head())
print(f"\nShape: {test.shape}")
print(f"Columns: {list(test.columns)}")

# use python inspect_data.py to run this script and see the output.
# Note that the test set has no "rating" column, which is what we're trying to predict.