from turtle import Screen
from snake_movement import SnakeMovement
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = SnakeMovement()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    snake.controls()

screen.exitonclick()
