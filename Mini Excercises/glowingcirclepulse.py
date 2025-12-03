import tkinter as tk
import math

root = tk.Tk()
root.title("Glowing Pulse")
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

r = 60
circle = canvas.create_oval(250-r, 250-r, 250+r, 250+r, fill="", outline="cyan", width=4)

def animate(t=0):
    scale = 1 + 0.2 * math.sin(t)
    new_r = r * scale
    canvas.coords(circle, 250-new_r, 250-new_r, 250+new_r, 250+new_r)
    root.after(20, animate, t+0.2)

animate()
root.mainloop()
