from turtle import Screen
from bars import Bars

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_bar = Bars((350, 0))
left_bar = Bars((-350, 0))

screen.listen()
screen.onkey(right_bar.up, "Up")
screen.onkey(right_bar.down, "Down")
screen.onkey(left_bar.up, "w")
screen.onkey(left_bar.down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
