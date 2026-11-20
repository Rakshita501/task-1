import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
df = pd.read_csv(project_folder / "outputs" / "cleaned_data" / "titanic_cleaned.csv")

total = len(df)
survivors = int(df["Survived"].sum())
survival_rate = df["Survived"].mean() * 100

class_rates = df.groupby("Pclass")["Survived"].mean() * 100
age_median = df["Age"].median()

report = f"""# Titanic Dataset: Key Findings

## Dataset
- Passengers analyzed: {total}
- Overall survival rate: {survival_rate:.1f}%
- Median passenger age: {age_median:.1f} years

## Findings
- {survivors} passengers survived; {total - survivors} did not.
- Passenger class survival rates:
"""

for passenger_class, rate in class_rates.items():
    report += f"  - Class {passenger_class}: {rate:.1f}% survived\\n"

report += """
## Data preparation
- Removed duplicate rows.
- Filled missing numeric values with each column's median.
- Filled missing text values with each column's most common value.

## Limitations
- Filling missing values with medians or common values may not reflect the original passenger information.
- Survival describes this dataset and should not be generalized to all sea disasters.

## Charts
See the `outputs/charts` folder for survival counts, survival by class, and age distribution.
"""

report_folder = project_folder / "report"
report_folder.mkdir(parents=True, exist_ok=True)
report_file = report_folder / "findings.md"
report_file.write_text(report, encoding="utf-8")

print("Report saved to:", report_file)
print(report)
