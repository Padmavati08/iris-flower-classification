
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
df = pd.read_csv("data/iris_cleaned.csv")

os.makedirs("reports/eda", exist_ok=True)

features = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

# 1. Species distribution
df["species"].value_counts().plot(
    kind="bar",
    title="Iris Species Distribution"
)
plt.xlabel("Species")
plt.ylabel("Number of Samples")
plt.tight_layout()
plt.savefig("reports/eda/species_distribution.png")
plt.close()

# 2. Feature distributions
df[features].hist(figsize=(9, 7), bins=15)
plt.suptitle("Distribution of Iris Features")
plt.tight_layout()
plt.savefig("reports/eda/feature_distributions.png")
plt.close()

# 3. Scatter plot
for feature_x, feature_y, filename in [
    ("sepal length (cm)", "sepal width (cm)", "sepal_scatter.png"),
    ("petal length (cm)", "petal width (cm)", "petal_scatter.png")
]:
    for species in df["species"].unique():
        subset = df[df["species"] == species]
        plt.scatter(
            subset[feature_x],
            subset[feature_y],
            label=species
        )

    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title("Iris Feature Relationship")
    plt.legend()
    plt.tight_layout()
    plt.savefig("reports/eda/" + filename)
    plt.close()

# 4. Correlation heatmap
correlation = df[features].corr()

plt.figure(figsize=(7, 5))
plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(label="Correlation")

plt.xticks(range(4), features, rotation=30, ha="right")
plt.yticks(range(4), features)

for i in range(4):
    for j in range(4):
        plt.text(
            j, i, f"{correlation.iloc[i, j]:.2f}",
            ha="center", va="center"
        )

plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("reports/eda/correlation_heatmap.png")
plt.close()

print("EDA completed successfully!")
print("Visualizations saved in reports/eda/")
