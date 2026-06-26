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
scoreboard.start_message()

game_is_on = True
game_started = False
game_paused = False


def start_game():
    global game_started
    scoreboard.clear()
    scoreboard.update_scoreboard()
    game_started = True

def pause_game():
    global game_paused

    if game_started:
        game_paused = not game_paused

        if game_paused:
            scoreboard.pause_message()
        else:
            scoreboard.clear()
            scoreboard.update_scoreboard()

def restart_game():
    snake.reset()
    scoreboard.reset()
    food.refresh()

    game_started = False
    game_paused = False

    scoreboard.start_message()

def close_game():
    global game_is_on
    game_is_on = False
    screen.bye()


def exit_game():
    scoreboard.clear()
    scoreboard.goto(0, 0)
    scoreboard.write("Thanks for Playing!", align="center", font=("Courier", 24, "bold"))
    screen.ontimer(close_game, 2000)




screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)
screen.onkey(key = "space", fun = start_game)
screen.onkey(key = "p", fun = pause_game)
screen.onkey(key = "r", fun = restart_game)
screen.onkey(key = "Escape", fun = exit_game)


while game_is_on:
    screen.update()

    if game_started and not game_paused:
        time.sleep(0.1)
        snake.move()

    #Detect collision with food.
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
            scoreboard.game_over()
            game_started = False


        # Detect collision with tail
        for segment in snake.segments[1:]:
            # if segment == snake.segments[0]: without slicing
            #     pass
            if snake.segments[0].distance(segment) < 10:
                game_started = False
                scoreboard.game_over()



    #if head collides with any segment in the tail:
    #trigger game_over
