from turtle import Screen
from bars import Bars
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
right_bar = Bars((350, 0))
left_bar = Bars((-350, 0))

screen.listen()
screen.onkey(right_bar.up, "Up")
screen.onkey(right_bar.down, "Down")
screen.onkey(left_bar.up, "w")
screen.onkey(left_bar.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_movement()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(right_bar) < 50
        and ball.xcor() > 320
        or ball.distance(left_bar) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()


screen.exitonclick()
