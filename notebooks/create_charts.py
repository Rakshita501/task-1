import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
data_file = project_folder / "outputs" / "cleaned_data" / "titanic_cleaned.csv"
charts_folder = project_folder / "outputs" / "charts"
charts_folder.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_file)
sns.set_theme(style="whitegrid")

# 1. Passenger survival counts
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Survived", hue="Survived", legend=False, palette="Set2")
plt.title("Titanic Passengers: Survival Counts")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig(charts_folder / "survival_counts.png", dpi=150)
plt.close()

# 2. Survival by passenger class
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Pclass", y="Survived", hue="Pclass", legend=False, palette="Blues")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig(charts_folder / "survival_by_class.png", dpi=150)
plt.close()

# 3. Age distribution
plt.figure(figsize=(7, 5))
sns.histplot(data=df, x="Age", bins=25, kde=True, color="teal")
plt.title("Passenger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig(charts_folder / "age_distribution.png", dpi=150)
plt.close()

print("Charts saved in:", charts_folder)
