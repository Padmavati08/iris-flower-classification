
import sqlite3

connection = sqlite3.connect("iris_database.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM predictions")
total = cursor.fetchone()[0]

print("Total predictions stored:", total)

cursor.execute("""
    SELECT prediction_id, sepal_length, sepal_width,
           petal_length, petal_width, model_name, created_at
    FROM predictions
    ORDER BY prediction_id DESC
    LIMIT 5
""")

print("\nPrediction Records:")
for record in cursor.fetchall():
    print(record)

connection.close()
