# draw circle of consistent size, have its tilt change
# each time it is drawn

from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.pen(pensize=2, speed=0)
Screen().colormode(255)


def rgb_generator():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def spirograph():
    for _ in range(75):
        tim.circle(50)
        tim.right(10)
        tim.pencolor(rgb_generator())


spirograph()

# She uses setheading(.heading()) instead of right()
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.pencolor(rgb_generator())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
# draw_spirograph(5)

screen = Screen()
screen.exitonclick()
