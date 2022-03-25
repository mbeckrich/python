import time
from turtle import Screen, xcor
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_generator()
    cars.car_movement()
    for car in cars.car_garage:
        if player.ycor() == car.xcor():
            game_is_on = False
