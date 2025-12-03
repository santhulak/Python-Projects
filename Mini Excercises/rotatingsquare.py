import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

for angle in range(0, 360, 5):
    t.clear()
    t.setheading(angle)
    for _ in range(4):
        t.forward(100)
        t.right(90)
