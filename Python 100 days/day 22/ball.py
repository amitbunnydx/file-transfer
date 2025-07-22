from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.fast = 0
        self.color('yellow')
        self.speed(self.fast)
        self.x_move=10
        self.y_move=10
        self.speed_fast=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move*= -1
        self.speed_fast*=0.9



    def bounce_x(self):
        self.x_move *= -1
        self.speed_fast*=0.9


    def reset(self):
        self.goto(0,0)
        self.speed_fast=0.1
        self.bounce_x()


# import package
# import turtle
#
# # loop for pattern
# for i in range(10):
#
# # set turtle speed
#     turtle.speed(10 - i)
#     # motion for pattern
#     turtle.forward(50 + 10 * i)
#     turtle.right(90)
