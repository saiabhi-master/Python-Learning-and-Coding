from turtle import Screen, time
from snake import Snake
from foody import Food
from scOreBoard import ScoreBoard

Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("Snake Game")
Screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()



Screen.listen()
Screen.onkey(snake.up,"Up")
Screen.onkey(snake.down, "Down")
Screen.onkey(snake.left, "Left")
Screen.onkey(snake.right, "Right")



game_on = True
while game_on:
    Screen.update()
    time.sleep(0.06)
    snake.move()

    #Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    #Detect Collision with wall
    if snake.head.xcor() > 660 or snake.head.xcor() < -660 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        game_on = False
        scoreboard.game_over()

    #Detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_on = False
    #         scoreboard.game_over()

    # Aliter

    check_seg = snake.segments[1:len(snake.segments)]
    for segment in check_seg:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


    #if head collides with any other segment ==>  Game Over
























Screen.exitonclick()
