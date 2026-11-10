
import tkinter as tk
from tkinter import ttk
import sqlite3


def load_data():
    for item in tree.get_children():
        tree.delete(item)

    connection = sqlite3.connect("iris_database.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT predictions.prediction_id,
               predictions.sepal_length,
               predictions.sepal_width,
               predictions.petal_length,
               predictions.petal_width,
               species.species_name,
               predictions.model_name,
               predictions.created_at
        FROM predictions
        JOIN species
        ON predictions.predicted_species_id = species.species_id
        ORDER BY predictions.prediction_id
    """)

    records = cursor.fetchall()

    for record in records:
        tree.insert("", tk.END, values=record)

    connection.close()

    count_label.config(
        text=f"Total prediction records: {len(records)}"
    )


root = tk.Tk()
root.title("Iris Database Viewer")
root.geometry("1050x400")

heading = tk.Label(
    root,
    text="IRIS PREDICTION DATABASE",
    font=("Arial", 16, "bold")
)
heading.pack(pady=15)

columns = (
    "ID", "Sepal Length", "Sepal Width",
    "Petal Length", "Petal Width",
    "Species", "Model", "Date"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for column in columns:
    tree.heading(column, text=column)
    tree.column(column, width=125, anchor="center")

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

count_label = tk.Label(root, font=("Arial", 11, "bold"))
count_label.pack(pady=5)

refresh_button = tk.Button(
    root,
    text="REFRESH RECORDS",
    command=load_data
)
refresh_button.pack(pady=10)

load_data()

root.mainloop()
