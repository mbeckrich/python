from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

bar = Turtle("square")
bar.penup()
bar.color("white")
bar.resizemode("user")
bar.shapesize(stretch_wid=5, stretch_len=1)
bar.goto(350, 0)


def up():
    new_y = bar.ycor() + 20
    return bar.goto(bar.xcor(), new_y)


def down():
    new_y = bar.ycor() - 20
    return bar.goto(bar.xcor(), new_y)


def bar_movement():
    screen.onkey(key="Up", fun=up)
    screen.onkey(key="Down", fun=down)


game_is_on = True
while game_is_on:
    screen.update()
    bar_movement()
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
