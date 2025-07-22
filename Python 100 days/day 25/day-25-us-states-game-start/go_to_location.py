import turtle
from turtle import Turtle

class State_Name(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.penup()
        self.hideturtle()
        self.speed(1)
        self.goto(-250,250)

        print('inside')
        # self.write(f'Count: {self.score} high score:{self.high_score}', align=ALIGNMENT, font=FONT)

    def go_to_location(self,name_is,x_axis,y_axis):
        self.goto(x_axis, y_axis)
        self.write(f'{name_is}', align='center', font=("Arial", 8, "normal"))
        # pass



