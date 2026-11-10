
import sqlite3

# Connect to the database
connection = sqlite3.connect("iris_database.db")

# Enable foreign key constraints
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()

# Table 1: Species
cursor.execute("""
CREATE TABLE IF NOT EXISTS species (
    species_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_name TEXT NOT NULL UNIQUE
)
""")

# Table 2: Flowers
cursor.execute("""
CREATE TABLE IF NOT EXISTS flowers (
    flower_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sepal_length REAL NOT NULL,
    sepal_width REAL NOT NULL,
    petal_length REAL NOT NULL,
    petal_width REAL NOT NULL,
    species_id INTEGER NOT NULL,
    FOREIGN KEY (species_id) REFERENCES species(species_id)
)
""")

# Table 3: Predictions
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sepal_length REAL NOT NULL,
    sepal_width REAL NOT NULL,
    petal_length REAL NOT NULL,
    petal_width REAL NOT NULL,
    predicted_species_id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (predicted_species_id)
        REFERENCES species(species_id)
)
""")

# Insert the three Iris species
species_list = [
    ("Iris-setosa",),
    ("Iris-versicolor",),
    ("Iris-virginica",)
]

cursor.executemany("""
INSERT OR IGNORE INTO species (species_name)
VALUES (?)
""", species_list)

connection.commit()

print("Database created successfully!")

# Display created tables
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table'
""")

print("\nDatabase tables:")
for table in cursor.fetchall():
    print(table[0])

connection.close()
