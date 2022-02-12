from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.xmove = 3
        self.ymove = 3
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1
        self.move_speed *= 0.9


    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9


    def both_bounce(self):
        self.xmove *= -1
        self.ymove *= -1

    def resetpos(self):
        self.goto(0, 0)
        self.move_speed = 0.01

