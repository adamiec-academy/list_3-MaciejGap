from turtle import *


def star():

    tracer(0, 1)

    update()

    for arm in range(10):

        for j in range(20):
            forward(10 + 3 * j)
            penup()
            backward(10 + 3 * j)
            right(360 / 10)
            forward(5)
            left(80)
            pendown()

    exitonclick()


star()
