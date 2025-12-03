import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

bubbles = []
for _ in range(20):
    x = random.randint(0, 500)
    y = random.randint(400, 500)
    r = random.randint(5, 20)
    bubbles.append([x, y, r])

def animate():
    canvas.delete("all")
    for b in bubbles:
        b[1] -= 2
        if b[1] < -50: b[1] = 500
        canvas.create_oval(b[0]-b[2], b[1]-b[2], b[0]+b[2], b[1]+b[2], outline="#00eaff", width=2)
    root.after(30, animate)

animate()
root.mainloop()
