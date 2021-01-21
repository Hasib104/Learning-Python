
from turtle import Turtle

STARTING_CO_ORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.squares_list = []
        self.create_snake()

    def create_snake(self):

        for counter in STARTING_CO_ORDINATES:
            self.add_snake(counter)

    def add_snake(self, counter):

        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(counter)
        self.squares_list.append(square)

    def extend(self):

        self.add_snake(self.squares_list[-1].position())

    def move_snake(self):

        for c in range(len(self.squares_list) - 1, 0, -1):  #Started from index 2 to 0, reducing 1
            new_x = self.squares_list[c - 1].xcor()
            new_y = self.squares_list[c - 1].ycor()
            self.squares_list[c].goto(new_x, new_y)

        self.squares_list[0].forward(MOVE_DISTANCE)

    def up(self):

        if self.squares_list[0].heading() != DOWN:
            self.squares_list[0].setheading(UP)

    def down(self):

        if self.squares_list[0].heading() != UP:
            self.squares_list[0].setheading(DOWN)

    def left(self):

        if self.squares_list[0].heading() != RIGHT:
            self.squares_list[0].setheading(LEFT)

    def right(self):

        if self.squares_list[0].heading() != LEFT:
            self.squares_list[0].setheading(RIGHT)