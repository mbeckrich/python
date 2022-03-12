from turtle import Screen
from bars import Bars

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
bars = Bars()

bars

screen.exitonclick()


# Background
# Dashed line down middle
# Scoreboard
# Moving bars
# width = 20, height = 100; x_pos = 350, y_pos = 0
# up and down keypress should move up/down 20px
# Moving ball
# If ball hits wall, bounce it off wall
# If bar is hit, send ball back in opposite direction
# If bar doesn't block, add scorepoint
