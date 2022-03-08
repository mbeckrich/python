from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

color = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle = ["turtle1", "turtle2", "turtle3", "turtle4", "turtle5", "turtle6"]
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which color turtle will win the race? Enter a color: ",
)


def turtle_gen():
    turtles = []
    for t in turtle:
        t = Turtle("turtle")
        t.penup()
        turtles.append(t)
    x_coord = -225
    y_coord = -75
    for n in range(0, 6):
        turtles[n].color(color[n])
        turtles[n].goto(x=x_coord, y=y_coord)
        y_coord += 25
    while True:
        for n in range(0, 6):
            turtles[n].forward(randint(0, 20))
            if turtles[n].position() >= (150, None):
                if color[n] == user_bet:
                    return print("You win!") and False
                return False


turtle_gen()

# turtle_1, turtle_2 are different 'instances'
# different instances can have different 'states'
# e.g. turtle_1.color = green and turtle_2.color = purple

# popup to bet color that will win the race
# turtles are in color of the rainbow
# once turtle crosses finish line, print win/loss bet
# in terminal

# textinput()

screen.exitonclick()
