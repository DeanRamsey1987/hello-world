import math
import turtle

def drawCircle(t, x, y, radius):
    t.penup()
    t.goto(x + radius, y)
    t.pendown()
    step = 2.0 * math.pi * radius / 120.0
    for _ in range(120):
        t.left(3)
        t.forward(step)

if __name__ == "__main__":
    t = turtle.Turtle()
    drawCircle(t, 0, 0, 100)
    turtle.done()
