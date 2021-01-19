
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_postions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for counter in range(0,6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[counter])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_postions[counter])
    all_turtles.append(new_turtle)

end_state = False
while not end_state:

    for turtle in all_turtles:

        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)

        if turtle.xcor() > 225:
            end_state = True
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()