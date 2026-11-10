
import sqlite3
import csv
import os

# Connect to database
connection = sqlite3.connect("iris_database.db")
cursor = connection.cursor()

os.makedirs("reports", exist_ok=True)

# Report 1: Species-wise flower count
cursor.execute("""
    SELECT species.species_name,
           COUNT(flowers.flower_id) AS total_flowers
    FROM species
    LEFT JOIN flowers
    ON species.species_id = flowers.species_id
    GROUP BY species.species_id, species.species_name
""")

species_data = cursor.fetchall()

with open("reports/species_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Species Name", "Total Flowers"])
    writer.writerows(species_data)

# Report 2: Prediction history
cursor.execute("""
    SELECT prediction_id, sepal_length, sepal_width,
           petal_length, petal_width,
           species.species_name, model_name, created_at
    FROM predictions
    JOIN species
    ON predictions.predicted_species_id = species.species_id
    ORDER BY prediction_id
""")

prediction_data = cursor.fetchall()

with open("reports/prediction_history.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "ID", "Sepal Length", "Sepal Width",
        "Petal Length", "Petal Width",
        "Predicted Species", "Model", "Date"
    ])
    writer.writerows(prediction_data)

connection.close()

print("Reports generated successfully!")
print("1. reports/species_report.csv")
print("2. reports/prediction_history.csv")
