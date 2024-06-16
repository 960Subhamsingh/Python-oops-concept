import turtle
bob = turtle.Turtle()
bob.speed(0)
def c():
    for i in range(360):
        bob.forward(i)
        bob.left(120)
c()