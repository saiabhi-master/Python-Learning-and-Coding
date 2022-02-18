from turtle import Turtle

class writer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.speed("fastest")

    def writer(self, x_cor, y_cor, note):
        self.goto(x_cor, y_cor)
        self.write(note, align="center", font=("Courier", 9, "normal"))

