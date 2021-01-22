
from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Cars:
    def __init__(self):
        self.cars_list = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(250, random_y)
            self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.backward(self.cars_speed)

    def lvl_up(self):
        self.cars_speed += MOVE_INCREMENT