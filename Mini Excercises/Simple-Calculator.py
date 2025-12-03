import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result: {num1 + num2}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result: {num1 - num2}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# GUI Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.config(bg="#1e1e1e")

# Labels
tk.Label(root, text="Enter First Number:", bg="#1e1e1e", fg="white").pack(pady=5)
entry1 = tk.Entry(root, width=20)
entry1.pack()

tk.Label(root, text="Enter Second Number:", bg="#1e1e1e", fg="white").pack(pady=5)
entry2 = tk.Entry(root, width=20)
entry2.pack()

# Buttons
tk.Button(root, text="Add", width=12, bg="#4caf50", fg="white", command=add_numbers).pack(pady=10)
tk.Button(root, text="Subtract", width=12, bg="#f44336", fg="white", command=subtract_numbers).pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Result: ", bg="#1e1e1e", fg="cyan", font=("Arial", 12))
result_label.pack(pady=15)

# Run App
root.mainloop()
