
import sqlite3

connection = sqlite3.connect("iris_database.db")
cursor = connection.cursor()

# Query 1: Display all flower species
print("\n1. FLOWER SPECIES")

cursor.execute("""
SELECT * FROM species
""")

for row in cursor.fetchall():
    print(row)


# Query 2: Count total flowers
print("\n2. TOTAL FLOWERS")

cursor.execute("""
SELECT COUNT(*) FROM flowers
""")

print("Total records:", cursor.fetchone()[0])


# Query 3: Display flower details with species names
print("\n3. FLOWER DETAILS")

cursor.execute("""
SELECT
    f.flower_id,
    f.sepal_length,
    f.sepal_width,
    f.petal_length,
    f.petal_width,
    s.species_name
FROM flowers f
JOIN species s
ON f.species_id = s.species_id
LIMIT 10
""")

for row in cursor.fetchall():
    print(row)


# Query 4: Count flowers belonging to each species
print("\n4. SPECIES-WISE FLOWER COUNT")

cursor.execute("""
SELECT s.species_name, COUNT(f.flower_id)
FROM species s
JOIN flowers f
ON s.species_id = f.species_id
GROUP BY s.species_name
""")

for row in cursor.fetchall():
    print(row)


connection.close()
