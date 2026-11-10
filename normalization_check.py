
import sqlite3

connection = sqlite3.connect("iris_database.db")
cursor = connection.cursor()

tables = ["species", "flowers", "predictions"]

for table in tables:
    print("\nTABLE:", table.upper())

    cursor.execute(f"PRAGMA table_info({table})")

    for column in cursor.fetchall():
        print(
            "Column:", column[1],
            "| Type:", column[2],
            "| Primary Key:", column[5]
        )

    cursor.execute(f"PRAGMA foreign_key_list({table})")

    for key in cursor.fetchall():
        print(
            "Foreign Key:", key[3],
            "->", key[2] + "." + key[4]
        )

connection.close()
