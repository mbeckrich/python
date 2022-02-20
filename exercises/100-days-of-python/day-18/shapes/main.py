# Overlay shapes: triangle, square, pentagon,
# hexagon, heptagon, octagon, nonagon, decagon
# 360/n of sides, e.g. 360/4 = 90, 360/5 = 72

from turtle import Turtle, Screen
from random import randrange

tim = Turtle()
tim.shape("turtle")
Screen().colormode(255)


def shape_calculator(full_circle, sides):
    while True:
        for _ in range(sides):
            tim.forward(100)
            tim.right(full_circle / sides)
            tim.pencolor(
                randrange(0.0, 256.0),
                randrange(0.0, 256.0),
                randrange(0.0, 256.0),
            )
        sides += 1
        if sides >= 11:
            return False


shape_calculator(full_circle=360, sides=3)

screen = Screen()
screen.exitonclick()
