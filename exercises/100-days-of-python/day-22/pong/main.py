from turtle import Screen
from bars import Bars
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
score = Score()
right_bar = Bars((350, 0))
left_bar = Bars((-350, 0))

screen.listen()
screen.onkey(right_bar.up, "Up")
screen.onkey(right_bar.down, "Down")
screen.onkey(left_bar.up, "w")
screen.onkey(left_bar.down, "s")

game_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
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

    if ball.xcor() > 380:
        ball.reset()
        score.left_point()

    if ball.xcor() < -380:
        ball.reset()
        score.right_point()


screen.exitonclick()
