STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.tilt(90)
        self.goto(0, -250)


    def move(self):
        new = self.ycor() + 15
        self.goto(0, new)

    def reset(self):
        self.goto(0, -250)


