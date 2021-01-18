
color_list = [(230, 215, 101), (154, 80, 38), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]

import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed("fastest")

no_dots = 100

tim.setheading(220)
tim.forward(500)
tim.setheading(0)

for counter in range(1, no_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if counter % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()