import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
df = pd.read_csv(project_folder / "data" / "titanic.csv")

print("Dataset size:", df.shape)
print("\nColumn types and non-missing values:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
