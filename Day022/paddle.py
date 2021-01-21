
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.left(90)
        self.goto(position)

    def up(self):

        if self.ycor() < 350:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):

        if self.ycor() > -340:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)