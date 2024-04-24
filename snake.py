import turtle
from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_arr = []
        self.create_snake()
        self.head = self.turtle_arr[0]

    def create_snake(self):
        for i in range(3):
            self.add_snake_length(i)

    def add_snake_length(self, i):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(i * (-20), 0)
        self.turtle_arr.append(new_turtle)

    # def extend(self):
    #     self.add_snake_length(self.turtle_arr[-1].position())
    def extend(self):
        last_position = self.turtle_arr[-1].position()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_position)
        self.turtle_arr.append(new_segment)

    def move_snake(self):
        for i in range(len(self.turtle_arr) - 1, 0, -1):
            new_x = self.turtle_arr[i - 1].xcor()
            nex_y = self.turtle_arr[i - 1].ycor()
            self.turtle_arr[i].goto(new_x, nex_y)
        self.head.forward(20)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



