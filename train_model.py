import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load cleaned dataset
df = pd.read_csv("data/iris_cleaned.csv")

# Separate features and target
X = df.drop("species", axis=1)
y = df["species"]

# Split data for evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create baseline Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train and evaluate
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("MODEL EVALUATION")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Retrain final model on the complete cleaned dataset
final_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

final_model.fit(X, y)

# Save final model
os.makedirs("models", exist_ok=True)

with open("models/iris_model.pkl", "wb") as file:
    pickle.dump(final_model, file)

print("\nFinal model trained on all 149 records.")
print("Model saved at models/iris_model.pkl")