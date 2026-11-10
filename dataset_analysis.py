
import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = [
    iris.target_names[i] for i in iris.target
]

print("1. DATASET INFORMATION")
print("Shape:", df.shape)
print("Columns:", list(df.columns))

print("\n2. MISSING VALUES")
print(df.isnull().sum())

print("\n3. DUPLICATE RECORDS")
print(df.duplicated().sum())

print("\n4. STATISTICAL SUMMARY")
print(df.describe())

print("\n5. SPECIES DISTRIBUTION")
print(df["species"].value_counts())

print("\n6. OUTLIER CHECK (IQR METHOD)")

for column in iris.feature_names:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    count = (
        (df[column] < lower) |
        (df[column] > upper)
    ).sum()

    print(column, ":", count, "potential outliers")

print("\nDataset inspection completed!")
