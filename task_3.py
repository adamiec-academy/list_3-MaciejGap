from turtle import *
import random


def mountain_height_change():
    return random.randint(5, 40)


def mountain_length_change():
    return random.randint(3, 30)


def mountains(length, height, mountain_range):

    for i in range(mountain_range):
        goto(length * i, mountain_height_change() + i * random.randint(5, 20))

    for i in range(mountain_range):
        goto(length * i + mountain_range * length, mountain_height_change() + (mountain_range - i) * random.randint(5, 20))


speed("slowest")

mountains(10, 50, 12)


exitonclick()
