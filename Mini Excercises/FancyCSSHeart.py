import tkinter as tk
import math

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

def animate(t=0):
    canvas.delete("all")
    for a in range(0, 360, 3):
        rad = math.radians(a)
        x = 16 * math.sin(rad)**3
        y = 13*math.cos(rad) - 5*math.cos(2*rad) - 2*math.cos(3*rad)
        x *= 10; y *= -10
        scale = 1 + 0.1*math.sin(t)
        canvas.create_oval(250+x*scale, 250+y*scale,
                           250+x*scale+3, 250+y*scale+3,
                           fill="red")
    root.after(30, animate, t+0.2)

animate()
root.mainloop()
