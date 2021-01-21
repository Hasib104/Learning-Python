
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((381, 0))
l_paddle = Paddle((-388, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

end_state = False
while not end_state:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detection with the wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_wall()

#detection with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 356 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_paddle()

#detection if r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

#detection if r_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()


