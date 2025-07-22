from turtle import Turtle,Screen
# from bord import ComputerBord,UserBord
from paddle import Paddle
from ball import Ball
from scoreboards import Scoreboard

import time

screen=Screen()
screen.screensize(300,300)
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)  # user to look snake properly It will blank screen

paddle_one=Paddle((300,0))
paddle_two=Paddle((-300,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(paddle_one.go_up,'Up')
screen.onkeypress(paddle_one.go_down,'Down')
screen.onkeypress(paddle_two.go_up,'w')
screen.onkeypress(paddle_two.go_down,'s')

start_game=True
while start_game:
    time.sleep(ball.speed_fast)
    # print(round(ball.speed_fast,2))
    screen.update()  # it will show snake
    ball.move()
    # print(ball.xcor())
    # print(ball.ycor())

    if ball.ycor()>250 or ball.ycor()<-250:
        print("collision")
        ball.bounce_y()


    if ball.distance(paddle_one)<50 and ball.xcor()>270 or ball.distance(paddle_two)<50 and ball.xcor()<-270:
        print("insideeee1")
        ball.bounce_x()

    if ball.xcor()>300:
        scoreboard.l_point()
        ball.reset()
        print('game over')


    if ball.xcor()<-300:
        scoreboard.r_point()
        ball.reset()
        print('game over')

screen.exitonclick()
