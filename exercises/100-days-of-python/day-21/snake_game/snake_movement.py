from turtle import Turtle, Screen

screen = Screen()
screen.listen()
SNAKE_PARTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
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
        for position in SNAKE_PARTS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.whole_snake.append(new_segment)

    def extend(self):
        self.add_segment(self.whole_snake[-1].position())

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
        screen.onkey(key="Up", fun=self.up)
        screen.onkey(key="Right", fun=self.right)
        screen.onkey(key="Left", fun=self.left)
        screen.onkey(key="Down", fun=self.down)
