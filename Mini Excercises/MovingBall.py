import tkinter as tk

root = tk.Tk()
root.title("Bouncing Ball")

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

ball = canvas.create_oval(10,10,50,50, fill="cyan")

dx, dy = 3, 3

def animate():
    global dx, dy
    canvas.move(ball, dx, dy)
    pos = canvas.coords(ball)

    if pos[0] <= 0 or pos[2] >= 400:
        dx = -dx
    if pos[1] <= 0 or pos[3] >= 400:
        dy = -dy

    root.after(10, animate)

animate()
root.mainloop()
