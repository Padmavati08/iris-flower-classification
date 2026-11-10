
import pandas as pd
import os
from sklearn.datasets import load_iris

# Load original dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = [
    iris.target_names[i] for i in iris.target
]

print("Original dataset:", df.shape)

# Remove duplicate records
df = df.drop_duplicates()

print("After removing duplicates:", df.shape)

# Save cleaned dataset
os.makedirs("data", exist_ok=True)
df.to_csv("data/iris_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")
