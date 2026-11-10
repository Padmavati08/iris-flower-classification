
import sqlite3
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Connect to our database
connection = sqlite3.connect("iris_database.db")
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()

# Insert flower records
for i in range(len(iris.data)):

    sepal_length = iris.data[i][0]
    sepal_width = iris.data[i][1]
    petal_length = iris.data[i][2]
    petal_width = iris.data[i][3]

    # Convert numerical target into species ID
    species_id = int(iris.target[i]) + 1

    cursor.execute("""
        INSERT INTO flowers (
            sepal_length,
            sepal_width,
            petal_length,
            petal_width,
            species_id
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        float(sepal_length),
        float(sepal_width),
        float(petal_length),
        float(petal_width),
        species_id
    ))

connection.commit()

# Check total records
cursor.execute("SELECT COUNT(*) FROM flowers")
total = cursor.fetchone()[0]

print("Iris dataset inserted successfully!")
print("Total flower records:", total)

# Display first five records
cursor.execute("""
    SELECT * FROM flowers LIMIT 5
""")

print("\nFirst five flower records:")
for record in cursor.fetchall():
    print(record)

connection.close()
