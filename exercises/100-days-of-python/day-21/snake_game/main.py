from turtle import Screen
from snake_movement import SnakeMovement
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = SnakeMovement()
food = Food()
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    snake.controls()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.calculate_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        score.game_over()

    for segment in snake.whole_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
