
from turtle import Turtle, Screen
from tim_the_turtle import Tim
from cars import Cars
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

tim = Tim()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tim.up, "w")

end_state = False
while not end_state:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

#collision with cars
    for car in cars.cars_list:
        if car.distance(tim) < 20:
            end_state = True
            scoreboard.game_over()

#cross finish line
    if tim.at_finish_line():
        tim.reset()
        cars.lvl_up()
        scoreboard.increase_lvl()

screen.exitonclick()