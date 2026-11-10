
import tkinter as tk
from tkinter import messagebox
from predict import predict_flower


def predict():
    try:
        sepal_length = float(entry_sepal_length.get())
        sepal_width = float(entry_sepal_width.get())
        petal_length = float(entry_petal_length.get())
        petal_width = float(entry_petal_width.get())

        result = predict_flower(
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        )

        result_label.config(
            text="Predicted Species: " + result
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numerical measurements."
        )
    except Exception as error:
        messagebox.showerror("Error", str(error))


def clear_fields():
    entry_sepal_length.delete(0, tk.END)
    entry_sepal_width.delete(0, tk.END)
    entry_petal_length.delete(0, tk.END)
    entry_petal_width.delete(0, tk.END)
    result_label.config(text="Prediction will appear here")


# Main window
root = tk.Tk()
root.title("Iris Flower Classification System")
root.geometry("450x480")
root.configure(bg="#f2f5fa")

# Heading
heading = tk.Label(
    root,
    text="IRIS FLOWER CLASSIFICATION",
    font=("Arial", 16, "bold"),
    bg="#f2f5fa",
    fg="#263859"
)
heading.pack(pady=20)

# Input form
form = tk.Frame(root, bg="#f2f5fa")
form.pack(pady=10)


def create_field(label_text, row):
    label = tk.Label(
        form,
        text=label_text,
        font=("Arial", 11),
        bg="#f2f5fa"
    )
    label.grid(row=row, column=0, padx=10, pady=10, sticky="w")

    entry = tk.Entry(form, font=("Arial", 11), width=18)
    entry.grid(row=row, column=1, padx=10, pady=10)

    return entry


entry_sepal_length = create_field("Sepal Length (cm)", 0)
entry_sepal_width = create_field("Sepal Width (cm)", 1)
entry_petal_length = create_field("Petal Length (cm)", 2)
entry_petal_width = create_field("Petal Width (cm)", 3)

# Buttons
tk.Button(
    root,
    text="PREDICT",
    command=predict,
    bg="#263859",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
).pack(pady=12)

tk.Button(
    root,
    text="CLEAR",
    command=clear_fields,
    font=("Arial", 10),
    width=15
).pack(pady=5)

# Prediction result
result_label = tk.Label(
    root,
    text="Prediction will appear here",
    font=("Arial", 12, "bold"),
    bg="#f2f5fa",
    fg="#263859"
)
result_label.pack(pady=20)

root.mainloop()
