import tkinter as tk
import math

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

def animate(t=0):
    canvas.delete("all")
    size = 50
    angle = t
    pts = []
    for i in range(4):
        rad = math.radians(angle + i*90)
        x = 150 + size * math.cos(rad)
        y = 150 + size * math.sin(rad)
        pts.append((x, y))
    canvas.create_polygon(pts, outline="#00eaff", fill="", width=4)
    root.after(30, animate, t+5)

animate()
root.mainloop()
