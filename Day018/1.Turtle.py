
"""#Importing Turtle and implementing"""
# from turtle import Turtle, Screen,
# #from turtle import * #It is advised to avoid impoting module like this
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("coral")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#
# for counter in range(4):
#     tim.forward(100)
#     tim.right(90)
#
#
#
#
# screen = Screen()
# screen.exitonclick()

"""#Installing modules"""
#
# import heroes
# print(heroes.gen())
# import villains

"""#Turtle dashline"""

# tim = Turtle()
# tim.shape("turtle")
# tim.color("coral")
#
# for counter in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
#
# screen = Screen()
# screen.exitonclick()

"""#Turtle different shapes"""

#lengthy

# tim = Turtle()
# tim.shape("turtle")
# tim.color("coral")
#
# def triangle():
#     tim.forward(100)
#     tim.right(120)
#     tim.forward(100)
#     tim.right(120)
#     tim.forward(100)
#     tim.right(120)
#
# def square():
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#
# def pentagon():
#     tim.forward(100)
#     tim.right(72)
#     tim.forward(100)
#     tim.right(72)
#     tim.forward(100)
#     tim.right(72)
#     tim.forward(100)
#     tim.right(72)
#     tim.forward(100)
#     tim.right(72)
#
# def hexagon():
#     tim.forward(100)
#     tim.right(60)
#     tim.forward(100)
#     tim.right(60)
#     tim.forward(100)
#     tim.right(60)
#     tim.forward(100)
#     tim.right(60)
#     tim.forward(100)
#     tim.right(60)
#     tim.forward(100)
#     tim.right(60)
#
# def heptagon():
#     tim.forward(100)
#     tim.right(51.43)
#     tim.forward(100)
#     tim.right(51.43)
#     tim.forward(100)
#     tim.right(51.43)
#     tim.forward(100)
#     tim.right(51.43)
#     tim.forward(100)
#     tim.right(51.43)
#     tim.forward(100)
#     tim.right(51.43)
#     tim.forward(100)
#     tim.right(51.43)
#
# def octagon():
#     tim.forward(100)
#     tim.right(45)
#     tim.forward(100)
#     tim.right(45)
#     tim.forward(100)
#     tim.right(45)
#     tim.forward(100)
#     tim.right(45)
#     tim.forward(100)
#     tim.right(45)
#     tim.forward(100)
#     tim.right(45)
#     tim.forward(100)
#     tim.right(45)
#     tim.forward(100)
#     tim.right(45)
#
# def nonagon():
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#     tim.forward(100)
#     tim.right(40)
#
# def decagon():
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#     tim.forward(100)
#     tim.right(36)
#
# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()
#
# screen = Screen()
# screen.exitonclick()

#short
import random

# tim = Turtle()
# tim.shape("turtle")
# tim.color("coral")
# colors = ["red", "black", "blue", "green"]
#
# def draw_shape(num_sides):
#
#     angle = 360 / num_sides
#     for counter in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for no_sides in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(no_sides)
#
#
# screen = Screen()
# screen.exitonclick()

"""#Turtle random movement"""

# tim = Turtle()
# tim.shape("turtle")
# tim.color("coral")
# colors = ["red", "black", "blue", "green", "coral", "brown"]
# direction = [0, 90, 180, 270]
# tim.width(15)
# tim.speed("fast")
#
#
# for no_sides in range(200):
#
#     tim.setheading(random.choice(direction))
#     tim.forward(30)
#     tim.color(random.choice(colors))
#
# screen = Screen()
# screen.exitonclick()

"""#Turtle random movement with different colors"""
# import turtle
#
# tim = turtle.Turtle()
# tim.shape("turtle")
# turtle.colormode(255)
# direction = [0, 90, 180, 270]
# tim.width(15)
# tim.speed("normal")
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# for no_sides in range(200):
#
#     tim.color(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(30)
#
# screen = Screen()
# screen.exitonclick()

"""#Turtle Spirograph"""

import turtle

tim = turtle.Turtle()
tim.shape("turtle")
turtle.colormode(255)

tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(gap_size):

    for counter in range(int(360 / gap_size)):

        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(3)

screen = turtle.Screen()
screen.exitonclick()