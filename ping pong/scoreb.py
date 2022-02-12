from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.L_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.R_score, align="center", font=("Courier", 70, "normal"))

    def Lscore(self):
        self.L_score += 1
        self.updatescore()

    def Rscore(self):
        self.R_score += 1
        self.updatescore()