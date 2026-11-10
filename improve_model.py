import pandas as pd
import os

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Load dataset
df = pd.read_csv("data/iris_cleaned.csv")

# Separate features and target
X = df.drop("species", axis=1)
y = LabelEncoder().fit_transform(df["species"])

# Same train-test split as previous experiment
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Baseline Random Forest
baseline = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

baseline.fit(X_train, y_train)
baseline_predictions = baseline.predict(X_test)

baseline_accuracy = accuracy_score(y_test, baseline_predictions)
baseline_f1 = f1_score(
    y_test, baseline_predictions, average="macro"
)

# Parameters to experiment with
parameter_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [None, 3, 5],
    "min_samples_split": [2, 4]
}

# Hyperparameter tuning
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    parameter_grid,
    cv=5,
    scoring="f1_macro",
    n_jobs=1
)

grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_
predictions = best_model.predict(X_test)

improved_accuracy = accuracy_score(y_test, predictions)
improved_f1 = f1_score(
    y_test, predictions, average="macro"
)

print("\nBASELINE RANDOM FOREST")
print("Accuracy:", round(baseline_accuracy * 100, 2), "%")
print("F1 Score:", round(baseline_f1 * 100, 2), "%")

print("\nBEST PARAMETERS")
print(grid_search.best_params_)

print("\nBEST CROSS-VALIDATION F1 SCORE")
print(round(grid_search.best_score_ * 100, 2), "%")

print("\nTUNED RANDOM FOREST")
print("Accuracy:", round(improved_accuracy * 100, 2), "%")
print("F1 Score:", round(improved_f1 * 100, 2), "%")

print("\nCLASSIFICATION REPORT")
print(classification_report(y_test, predictions))

# Save experiment results
results = pd.DataFrame([
    {
        "Model": "Baseline Random Forest",
        "Accuracy": round(baseline_accuracy * 100, 2),
        "F1 Score": round(baseline_f1 * 100, 2)
    },
    {
        "Model": "Tuned Random Forest",
        "Accuracy": round(improved_accuracy * 100, 2),
        "F1 Score": round(improved_f1 * 100, 2)
    }
])

os.makedirs("reports", exist_ok=True)
results.to_csv("reports/model_improvement.csv", index=False)

print("\nExperiment saved in reports/model_improvement.csv")