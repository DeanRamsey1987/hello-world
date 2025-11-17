import turtle

def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        d = distance / 3.0
        drawFractalLine(t, d, angle, level - 1)
        drawFractalLine(t, d, angle + 60, level - 1)
        drawFractalLine(t, d, angle - 60, level - 1)
        drawFractalLine(t, d, angle, level - 1)

if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    size = 500
    level = 3
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    drawFractalLine(t, size, 0, level)
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)
    turtle.done()
