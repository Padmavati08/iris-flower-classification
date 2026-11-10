
import sqlite3

connection = sqlite3.connect("iris_database.db")
cursor = connection.cursor()

# 1. SELECT: Display all species
print("\n1. ALL SPECIES")
cursor.execute("SELECT * FROM species")
print(cursor.fetchall())

# 2. WHERE: Filter flowers
print("\n2. FLOWERS WITH PETAL LENGTH > 5")
cursor.execute("""
    SELECT flower_id, petal_length
    FROM flowers
    WHERE petal_length > 5
""")
print(cursor.fetchall())

# 3. ORDER BY: Sort flowers
print("\n3. FLOWERS SORTED BY SEPAL LENGTH")
cursor.execute("""
    SELECT flower_id, sepal_length
    FROM flowers
    ORDER BY sepal_length DESC
    LIMIT 10
""")
print(cursor.fetchall())

# 4. JOIN: Combine flower and species tables
print("\n4. FLOWER AND SPECIES DETAILS")
cursor.execute("""
    SELECT flowers.flower_id, species.species_name
    FROM flowers
    JOIN species
    ON flowers.species_id = species.species_id
    LIMIT 10
""")
print(cursor.fetchall())

# 5. GROUP BY: Count flowers by species
print("\n5. SPECIES-WISE FLOWER COUNT")
cursor.execute("""
    SELECT species.species_name, COUNT(flowers.flower_id)
    FROM species
    LEFT JOIN flowers
    ON species.species_id = flowers.species_id
    GROUP BY species.species_id, species.species_name
""")
print(cursor.fetchall())

# 6. Aggregate function
print("\n6. AVERAGE SEPAL LENGTH")
cursor.execute("SELECT AVG(sepal_length) FROM flowers")
print(cursor.fetchone())

connection.close()
