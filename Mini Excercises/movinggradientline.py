import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=200, bg="black")
canvas.pack()

x = 0
def animate():
    global x
    canvas.delete("all")
    colors = ["#ff0099", "#00e5ff", "#00ff66"]
    canvas.create_line(0, 100, 500, 100, fill=colors[x % 3], width=8)
    x += 1
    root.after(120, animate)

animate()
root.mainloop()
