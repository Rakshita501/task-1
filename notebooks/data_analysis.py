import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
csv_path = project_folder / "data" / "titanic.csv"

df = pd.read_csv(csv_path)

print("Dataset loaded successfully!")
print("Rows and columns:", df.shape)
print(df.head())
