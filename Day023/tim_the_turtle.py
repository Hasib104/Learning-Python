
from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 250


class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("coral")
        self.penup()
        self.left(90)
        self.reset()

    def up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def reset(self):
        self.goto(STARTING_POS)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False