import time
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from Food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake_game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_left, "a")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
        scoreboard.update()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False

    for segment in snake.turtle_arr:
        if segment != snake.head:
            if snake.head.distance(segment) < 5:
                game_is_on = False

scoreboard.game_over()

screen.exitonclick()
