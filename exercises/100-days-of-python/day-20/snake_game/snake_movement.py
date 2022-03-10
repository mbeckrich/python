from turtle import Turtle, Screen

SNAKE_PARTS = ["snake_head", "snake_body", "snake_tail"]
MOVE_DISTANCE = 20
SCREEN = Screen()
SCREEN.listen()
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class SnakeMovement:
    """Creates the body of the snake and how it moves."""

    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.head = self.whole_snake[0]

    def create_snake(self):
        for parts in SNAKE_PARTS:
            body_part = Turtle("square")
            body_part.color("white")
            body_part.penup()
            self.whole_snake.append(body_part)

    def move(self):
        for segment in range(len(self.whole_snake) - 1, 0, -1):
            snake_x = self.whole_snake[segment - 1].xcor()
            snake_y = self.whole_snake[segment - 1].ycor()
            self.whole_snake[segment].goto(snake_x, snake_y)
        self.whole_snake[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)

    def controls(self):
        SCREEN.onkey(key="Up", fun=self.up)
        SCREEN.onkey(key="Right", fun=self.right)
        SCREEN.onkey(key="Left", fun=self.left)
        SCREEN.onkey(key="Down", fun=self.down)
