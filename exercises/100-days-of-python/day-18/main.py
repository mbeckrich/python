from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("black", "green")

# My attempt:


def dashed_line(total_trip, distance, line_color, alt_line_color):
    while total_trip <= total_trip:
        for _ in range(distance):
            tim.pencolor(alt_line_color)
            tim.forward(distance * 0.5)
            tim.pencolor(line_color)
            tim.forward(distance * 0.5)
        for _ in range(distance):
            tim.pencolor(line_color)
            tim.forward(distance)
        for _ in range(distance):
            tim.pencolor(alt_line_color)
            tim.forward(distance)
        tim.pencolor(line_color)
        tim.forward(distance * 0.5)


dashed_line(
    total_trip=15, distance=10, line_color="white", alt_line_color="black"
)

# Hers (does this require loop she does not include?)
# She uses pendown(), penup()

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Keep at the bottom
screen = Screen()
screen.exitonclick()
