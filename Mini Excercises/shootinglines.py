import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

ripples = []

def click(event):
    ripples.append([event.x, event.y, 1])

canvas.bind("<Button-1>", click)

def animate():
    canvas.delete("all")
    for r in ripples:
        canvas.create_oval(r[0]-r[2], r[1]-r[2],
                           r[0]+r[2], r[1]+r[2],
                           outline="cyan")
        r[2] += 3
        if r[2] > 120: ripples.remove(r)
    root.after(30, animate)

animate()
root.mainloop()
