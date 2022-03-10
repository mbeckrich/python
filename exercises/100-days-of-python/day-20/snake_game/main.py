from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake_parts = ["snake_head", "snake_body", "snake_tail"]
whole_snake = []
snake_x = 0
snake_y = 0

for snake in snake_parts:
    body_part = Turtle("square")
    body_part.color("white")
    body_part.penup()
    whole_snake.append(body_part)

while True:
    time.sleep(0.1)
    screen.update()
    for segment in range(len(whole_snake) - 1, 0, -1):
        snake_x = whole_snake[segment - 1].xcor()
        snake_y = whole_snake[segment - 1].ycor()
        whole_snake[segment].goto(snake_x, snake_y)
    whole_snake[0].forward(20)
    whole_snake[0].left(90)


screen.exitonclick()

# she creates three parts manually instead of using a for loop
# she creates for loop using tuples
# for position in starting_position: [(0,0), (-20, 0), (-40, 0)]
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)
