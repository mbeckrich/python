from turtle import Turtle, Screen
from random import choice

hirst = Turtle()
hirst.shape = "arrow"
hirst.penup()
Screen().colormode(255)
hirst.goto(-200, -200)

color_list = [
    (244, 237, 222),
    (243, 234, 240),
    (232, 242, 237),
    (192, 165, 115),
    (138, 166, 190),
    (56, 102, 140),
    (141, 91, 50),
    (12, 23, 55),
    (222, 207, 123),
    (182, 154, 42),
    (61, 22, 11),
    (182, 146, 165),
    (142, 177, 151),
    (72, 117, 81),
    (58, 15, 26),
    (126, 79, 102),
    (130, 30, 16),
    (15, 39, 23),
    (24, 53, 127),
    (177, 188, 215),
    (164, 104, 134),
    (115, 31, 46),
    (97, 150, 100),
    (98, 121, 172),
    (210, 178, 197),
    (174, 105, 93),
    (74, 150, 165),
    (25, 91, 65),
    (172, 205, 180),
]


def hirst_painting():
    for _ in range(10):
        for _ in range(10):
            hirst.forward(50)
            hirst.dot(20, choice(color_list))
        hirst.left(90)
        hirst.forward(50)
        hirst.right(90)
        hirst.back(500)
    hirst.hideturtle()


hirst_painting()

screen = Screen()
screen.exitonclick()
