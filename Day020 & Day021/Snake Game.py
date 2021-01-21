
from turtle import Turtle, Screen
from snake_class import Snake
import time
from food_class import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

end_state = False
while not end_state:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

#collision detection

    if snake.squares_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
#collision with walls

    if snake.squares_list[0].xcor() > 280 or snake.squares_list[0].xcor() < -300 or snake.squares_list[0].ycor() > 300 or snake.squares_list[0].ycor() < -280:
        end_state = True
        scoreboard.game_over()

#collsion with wall

    for counter in snake.squares_list[1:]:

        if snake.squares_list[0].distance(counter) < 10:
            end_state = True
            scoreboard.game_over()

screen.exitonclick()


