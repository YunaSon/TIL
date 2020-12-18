import turtle
t = turtle.Pen()

color = ['red', 'blue', 'green', 'salmon', 'lemon chiffon']

t.pencolor(color[4])
for x in range(100):
    t.forward(x)
    t.left(91)