
import pickle
import sqlite3
import pandas as pd

# Load the final trained model
with open("models/iris_model.pkl", "rb") as file:
    model = pickle.load(file)


def predict_flower(sepal_length, sepal_width,
                   petal_length, petal_width):

    # Prepare input with the original feature names
    measurements = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)"
        ]
    )

    # Predict species name directly
    prediction = model.predict(measurements)[0]

    # Map species names to database IDs
    species_ids = {
        "setosa": 1,
        "versicolor": 2,
        "virginica": 3
    }

    predicted_species_id = species_ids[prediction]

    # Format display name
    predicted_species = "Iris-" + prediction

    # Save prediction in SQLite
    with sqlite3.connect("iris_database.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO predictions
            (sepal_length, sepal_width, petal_length,
             petal_width, predicted_species_id, model_name)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            sepal_length,
            sepal_width,
            petal_length,
            petal_width,
            predicted_species_id,
            "Random Forest"
        ))

    return predicted_species
