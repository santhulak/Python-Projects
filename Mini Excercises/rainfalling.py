import tkinter as tk
import random
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.pack()
drops = [canvas.create_line(0,0,0,10, fill="cyan") for _ in range(40)]
def animate():
    for d in drops:
        canvas.move(d, 0, random.randint(5,10))
        if canvas.coords(d)[1] > 300:
            canvas.coords(d, random.randint(0,300), 0,
                               random.randint(0,300), 10)
    root.after(30, animate)
animate()
root.mainloop()
