from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update()
        self.hideturtle()
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))

    def increase(self):
        self.score+=1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))