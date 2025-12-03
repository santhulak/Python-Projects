import turtle, time
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "yellow", "cyan", "magenta", "white"]

for i in range(200):
    t.color(colors[i % len(colors)])
    t.forward(i)
    t.left(91)

turtle.done()
