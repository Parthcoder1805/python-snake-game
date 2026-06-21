from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.game_over()
        game_is_on = False


    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.segments[0]: without slicing
        #     pass
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



    #if head collides with any segment in the tail:
    #trigger game_over


screen.exitonclick()