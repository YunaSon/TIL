import turtle

angles = [91, 46, 61, 121]

t = turtle.Pen()
for x in range(100):
    t.forward(x)
    t.left(angles[0])

