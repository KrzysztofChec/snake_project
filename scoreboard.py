from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        if not os.path.exists("best_score.txt"):
            with open("best_score.txt", 'w') as file:
                file.write("0")
                self.highscore = 0
        else:
            with open("best_score.txt",'r') as file:
                self.highscore = int(file.read())
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 280)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align="center", font=("Courier", 12, "normal"))

    def increase(self):
        self.score += 1

    def reset(self):
        if self.score > self.highscore:
            with open("best_score.txt",'w') as file:
                file.write(str(self.score))
            print(" w ifie ")
            self.highscore = self.score
        self.score = 0


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
