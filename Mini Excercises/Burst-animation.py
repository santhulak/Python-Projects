import turtle, random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "yellow", "orange", "white"]

for burst in range(20):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color(random.choice(colors))

    for _ in range(20):
        t.forward(random.randint(50,150))
        t.backward(random.randint(50,150))
        t.right(18)
