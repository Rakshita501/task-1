import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "data" / "titanic.csv"
output_folder = project_folder / "outputs" / "cleaned_data"
output_folder.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

before = len(df)
df = df.drop_duplicates()
print("Duplicate rows removed:", before - len(df))

# Fill numeric columns with their median
numeric_columns = df.select_dtypes(include="number").columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill text columns with the most common value, or "Unknown" if empty
text_columns = df.select_dtypes(include="object").columns
for column in text_columns:
    if df[column].isna().any():
        mode = df[column].mode()
        fill_value = mode.iloc[0] if not mode.empty else "Unknown"
        df[column] = df[column].fillna(fill_value)

output_file = output_folder / "titanic_cleaned.csv"
df.to_csv(output_file, index=False)

print("Remaining missing values:", int(df.isna().sum().sum()))
print("Cleaned file saved to:", output_file)
