import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
tom = Player()
screen.onkey(tom.move, "Up")
carmanager = CarManager()
score_board = Scoreboard()

writer = Turtle()
writer.hideturtle()



game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()



    #Detect collision with Car
    for i in carmanager.all_cars:
        if tom.distance(i) < 15:
            game_is_on = False
            writer.penup()
            writer.goto(0, 0)
            writer.write("Game Over!", align="center", font=("Courier", 70, "normal"))

    #Detect Round win
    if tom.ycor() > 250:
        score_board.update()
        carmanager.level_up()
        tom.reset()




screen.exitonclick()