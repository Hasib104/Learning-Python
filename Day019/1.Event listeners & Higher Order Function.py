
"""#Basic event listener & Higher order function"""
from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()
#
# def move_forward():
#     tim.forward(20)
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forward)
# screen.exitonclick()

"""#Etch-A-Sketch"""

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_clockwise():
    tim.setheading(tim.heading() - 10)

def turn_counterclockwise():
    tim.setheading(tim.heading() + 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()