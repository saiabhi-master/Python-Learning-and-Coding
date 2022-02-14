FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("black")
        self.goto(-210, 235)
        self.write(f"Level: {self.score}", align="center", font=FONT)



    def update(self):
        self.goto(-210, 235)
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center", font=FONT)





