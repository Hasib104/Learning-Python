
from turtle import Turtle
FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-150, 300)
        self.write(f"L:{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(150, 300)
        self.write(f"R:{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()