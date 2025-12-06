import tkinter as tk

# ---------- Update the face based on mood ----------
def update_mood(mood):
    canvas.delete("all")

    # Default face color
    face_color = "yellow"

    # Change facial expression based on mood
    if mood == "Happy":
        eye = "black"
        mouth_style = "smile"
        face_color = "yellow"

    elif mood == "Sad":
        eye = "black"
        mouth_style = "sad"
        face_color = "#f7d47d"

    elif mood == "Angry":
        eye = "red"
        mouth_style = "angry"
        face_color = "#ffcc00"

    elif mood == "Surprised":
        eye = "black"
        mouth_style = "o"
        face_color = "lightyellow"

    # ----- Draw Face -----
    canvas.create_oval(50, 50, 250, 250, fill=face_color, outline="black", width=3)

    # ----- Eyes -----
    canvas.create_oval(100, 110, 130, 140, fill=eye)
    canvas.create_oval(170, 110, 200, 140, fill=eye)

    # ----- Mouth -----
    if mouth_style == "smile":
        canvas.create_arc(100, 140, 200, 210, start=180, extent=180, width=3, style=tk.ARC)

    elif mouth_style == "sad":
        canvas.create_arc(100, 160, 200, 240, start=0, extent=180, width=3, style=tk.ARC)

    elif mouth_style == "angry":
        # Angry eyebrows
        canvas.create_line(95, 100, 130, 120, width=4)
        canvas.create_line(205, 100, 170, 120, width=4)
        canvas.create_rectangle(120, 170, 180, 190, fill="black")

    elif mouth_style == "o":
        canvas.create_oval(135, 160, 165, 190, fill="black")

# ---------- GUI Window ----------
root = tk.Tk()
root.title("Cartoon Mood Face")
root.geometry("320x400")
root.configure(bg="white")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Default mood
update_mood("Happy")

# ---------- Mood Buttons ----------
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

moods = ["Happy", "Sad", "Angry", "Surprised"]

for mood in moods:
    btn = tk.Button(button_frame, text=mood, width=10, command=lambda m=mood: update_mood(m))
    btn.pack(side="left", padx=5)

root.mainloop()
