from turtle import Turtle, Screen
from random import randrange, choice

tim = Turtle()
tim.shape("turtle")
tim.pen(pensize=10, speed=0)
Screen().colormode(255)
right_angles = [0, 90, 180, 270]


def random_walk():
    for _ in range(100):
        tim.forward(25)
        tim.right(choice(right_angles))
        tim.pencolor(
            randrange(0.0, 256.0),
            randrange(0.0, 256.0),
            randrange(0.0, 256.0),
        )


random_walk()

screen = Screen()
screen.exitonclick()

# She uses setheading instead of right()
# She introduces tuples here for random rgbs
# Uses a function to create the rgb tuple
