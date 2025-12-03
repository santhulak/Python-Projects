import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

stars = [[random.randint(0,500), random.randint(0,500), random.randint(1,3)] for _ in range(80)]

def animate():
    canvas.delete("all")
    for s in stars:
        s[1] += s[2]
        if s[1] > 500: s[1] = 0
        canvas.create_oval(s[0], s[1], s[0]+s[2], s[1]+s[2], fill="white")
    root.after(30, animate)

animate()
root.mainloop()
