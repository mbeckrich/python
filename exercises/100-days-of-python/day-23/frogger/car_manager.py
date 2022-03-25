from turtle import Turtle, position
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_garage = []

    def car_generator(self):
        random_speed = random.randint(1, 6)
        if random_speed == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 240)
            car.goto(300, random_y)
            self.car_garage.append(car)

    def car_movement(self):
        for car in self.car_garage:
            car.backward(STARTING_MOVE_DISTANCE)
