from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()
turtle.speed(0)


def move_forward():
    return turtle.forward(10)


def move_backward():
    return turtle.backward(10)


def clockwise():
    return turtle.right(10)


def counter_clockwise():
    return turtle.left(10)


# she uses heading instead of right/left
# heading()+10
# did not catch request for this function:
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
# use keyword argument rather than positional when
# using 3rd party higher order functions
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
