from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet!", prompt="which turtle do u think will win? Pick color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []



for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

import random


while is_race_on:
    for turt in all_turtles:
        if turt.xcor() > 220:
            is_race_on = False
            win_col = turt.pencolor()
            if win_col == user_bet:
                print(f"You win! {win_col} turtle won!")
            else:
                print(f"You lose! {win_col} turtle won!")

        randis = random.randint(0, 10)
        turt.forward(randis)


















screen.exitonclick()