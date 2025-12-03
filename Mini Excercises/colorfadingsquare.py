import turtle, time

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

for size in range(20, 200, 5):
    t.color((size/200, 0, 1))
    for _ in range(4):
        t.forward(size)
        t.right(90)
