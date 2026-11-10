import pickle
import pandas as pd

# Load final trained model
with open("models/iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# Test sample
sample = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ]
)

# Predict species
prediction = model.predict(sample)

print("Input measurements:", sample.values.tolist()[0])
print("Predicted Iris species:", prediction[0])