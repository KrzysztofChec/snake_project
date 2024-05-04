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

time_speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(time_speed)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        if time_speed > 9.5:
            time_speed = time_speed - 0.004
        food.refresh()
        snake.extend()
        scoreboard.increase()
        scoreboard.update()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: # miejsce kolizji ze sciana
        print("granica")
        scoreboard.reset()
        scoreboard.update()
        snake.reset()

    for segment in snake.turtle_arr[1:]: # miejsce kolizjiu weza z samymm soba
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            scoreboard.update()
            snake.reset()

screen.exitonclick()
