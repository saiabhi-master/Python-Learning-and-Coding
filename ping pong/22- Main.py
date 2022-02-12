from turtle import Turtle, Screen
from Paddle import paddle
from ball import Ball
import time
from scoreb import ScoreBoard

Screen = Screen()
Screen.bgcolor("black")
Screen.setup(width=800, height=600)
Screen.title("PONG")
Screen.tracer(0)

paddleR = paddle(350)
paddleL = paddle(-350)
billy = Ball()
scoreboard = ScoreBoard()


Screen.listen()
Screen.onkey(paddleR.go_up, "Up")
Screen.onkey(paddleR.go_down, "Down")
Screen.onkey(paddleL.go_up, "w")
Screen.onkey(paddleL.go_down, "s")

game = True
while game:
    time.sleep(billy.move_speed)
    Screen.update()
    billy.move()

    #detect collision with ball
    if billy.ycor() > 280 or billy.ycor() < -280:
        billy.bounce_y()



    #detect collision with paddles
    if billy.distance(paddleR) < 50 and billy.xcor() > 340:
        billy.bounce_x()


    if billy.distance(paddleL) < 50 and billy.xcor() < -340:
        billy.bounce_x()


    #if right player misses
    if billy.xcor() > 380:
        billy.resetpos()
        billy.bounce_x()
        scoreboard.Lscore()

    #if left player misses
    if billy.xcor() < -380:
        billy.resetpos()
        billy.bounce_x()
        scoreboard.Rscore()


Screen.exitonclick()

