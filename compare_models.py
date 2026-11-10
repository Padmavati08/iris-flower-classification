import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Load cleaned dataset
df = pd.read_csv("data/iris_cleaned.csv")

# Separate features and target
X = df.drop("species", axis=1)
y = LabelEncoder().fit_transform(df["species"])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Define models
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),

    "Decision Tree": DecisionTreeClassifier(random_state=42),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

results = []

# Train and evaluate each model
for name, model in models.items():

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test, predictions, average="macro"
    )
    recall = recall_score(
        y_test, predictions, average="macro"
    )
    f1 = f1_score(
        y_test, predictions, average="macro"
    )

    results.append({
        "Algorithm": name,
        "Accuracy": round(accuracy * 100, 2),
        "Precision": round(precision * 100, 2),
        "Recall": round(recall * 100, 2),
        "F1 Score": round(f1 * 100, 2)
    })

    print("\n", "=" * 40)
    print("Algorithm:", name)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

# Save comparison results
results_df = pd.DataFrame(results)

os.makedirs("reports", exist_ok=True)
results_df.to_csv("reports/model_comparison.csv", index=False)

print("\nFINAL MODEL COMPARISON")
print(results_df.to_string(index=False))

print("\nResults saved in reports/model_comparison.csv")