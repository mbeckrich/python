from turtle import Turtle, Screen

screen = Screen()
screen.listen()


class Bars:
    def __init__(self):
        self.bar_generator()

    def bar_generator(self):
        right_bar = Turtle("square")
        right_bar.penup()
        right_bar.color("white")
        right_bar.resizemode("user")
        right_bar.shapesize(5, 1)
        right_bar.goto(350, 0)
        left_bar = Turtle("square")
        left_bar.penup()
        left_bar.color("white")
        left_bar.resizemode("user")
        left_bar.shapesize(5, 1)
        left_bar.goto(-350, 0)
