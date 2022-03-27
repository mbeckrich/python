import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_generator()
    cars.car_movement()

    for car in cars.car_garage:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.finish_line():
        player.return_to_start()
        cars.speed_increase()
        scoreboard.update_scoreboard()

screen.exitonclick()
