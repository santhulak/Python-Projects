import turtle, random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("red")

for _ in range(200):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.forward(random.randint(50, 200))
    t.right(random.randint(10, 40))
