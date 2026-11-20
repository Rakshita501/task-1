# Titanic Dataset: Key Findings

## Dataset
- Passengers analyzed: 891
- Overall survival rate: 38.4%
- Median passenger age: 28.0 years

## Findings
- 342 passengers survived; 549 did not.
- Passenger class survival rates:
  - Class 1: 63.0% survived\n  - Class 2: 47.3% survived\n  - Class 3: 24.2% survived\n
## Data preparation
- Removed duplicate rows.
- Filled missing numeric values with each column's median.
- Filled missing text values with each column's most common value.

## Limitations
- Filling missing values with medians or common values may not reflect the original passenger information.
- Survival describes this dataset and should not be generalized to all sea disasters.

## Charts
See the `outputs/charts` folder for survival counts, survival by class, and age distribution.
