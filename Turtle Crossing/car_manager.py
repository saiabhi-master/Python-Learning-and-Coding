COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-150, 200)
            new_car.goto(250, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    # def __init__(self):
    #     super().__init__()
    #
    #     self.shape("square")
    #     self.color(random.choice(COLORS))
    #     self.penup()
    #     self.goto(250, )
    #     self.shapesize(stretch_wid=1, stretch_len=2)
    #
    # def keep_moving(self):
    #     new = self.xcor() - 10
    #     self.goto(new, 0)

