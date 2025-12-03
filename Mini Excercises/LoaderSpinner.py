import tkinter as tk
import math

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

def animate(t=0):
    canvas.delete("all")
    for i in range(8):
        angle = t + i * (math.pi/4)
        x = 200 + 80 * math.cos(angle)
        y = 200 + 80 * math.sin(angle)
        canvas.create_oval(x-8, y-8, x+8, y+8, fill="cyan")
    root.after(40, animate, t+0.2)

animate()
root.mainloop()
