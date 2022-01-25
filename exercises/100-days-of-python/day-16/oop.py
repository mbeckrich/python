from turtle import Turtle, Screen

# timmy object created from turtle.Turtle() class
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen")
timmy.forward(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
