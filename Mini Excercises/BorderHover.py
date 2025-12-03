import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="black")
canvas.pack()

border = canvas.create_rectangle(50, 50, 350, 250, outline="#333", width=6)

def glow(t=0):
    neon = ["#0ff", "#6ff", "#9ff", "#cff"]
    canvas.itemconfig(border, outline=neon[t % 4])
    root.after(150, glow, t+1)

glow()
root.mainloop()
