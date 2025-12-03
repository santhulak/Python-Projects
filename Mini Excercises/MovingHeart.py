import turtle, math, time

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

for size in range(80, 150):
    t.color("red")
    t.penup()
    t.goto(0, -size)
    t.pendown()

    t.begin_fill()
    for i in range(360):
        x = size * math.sin(i) ** 3
        y = size * math.cos(i) - math.cos(2*i)/2 - math.cos(3*i)/6
        t.goto(x, y)
    t.end_fill()
    t.clear()

turtle.done()




