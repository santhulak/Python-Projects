import tkinter as tk
from tkinter import messagebox

# Mood mapping based on first letter
def analyze_mood():
    name = entry.get().strip()
    
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name.")
        return
    
    first = name[0].lower()

    # Mood rules (You can edit these!)
    if first in "abc":
        mood = "You are Calm 😊"
    elif first in "def":
        mood = "You are Energetic ⚡"
    elif first in "ghi":
        mood = "You are Creative 🎨"
    elif first in "jkl":
        mood = "You are Kind 💛"
    elif first in "mno":
        mood = "You are Powerful 💥"
    elif first in "pqr":
        mood = "You are Joyful 😄"
    elif first in "stu":
        mood = "You are Thoughtful 🤔"
    elif first in "vwx":
        mood = "You are Adventurous 🧭"
    else:  # y, z
        mood = "You are Unique 🌟"

    result_label.config(text=mood, fg="white")

# ---------------- GUI Design ---------------- #

root = tk.Tk()
root.title("Name Mood Analyzer")
root.geometry("380x260")
root.configure(bg="#1e1e1e")

title_label = tk.Label(
    root,
    text="Enter your Name",
    fg="cyan",
    bg="#1e1e1e",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16), width=18, justify="center")
entry.pack(pady=10)

analyze_btn = tk.Button(
    root,
    text="Analyze Mood",
    font=("Arial", 14, "bold"),
    bg="purple",
    fg="white",
    command=analyze_mood
)
analyze_btn.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    fg="white",
    bg="#1e1e1e",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=20)

root.mainloop()
