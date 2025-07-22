import turtle
from turtle import Turtle

RIGHT_SEGMENT_LOCATION=[(300,20),(300,0),(300,-20)]
LEFT_SEGMENT_LOCATION=[(-300,20),(-300,0),(-300,-20)]


MOVE_DISTANCE=20


class ComputerBord:
    def __init__(self):
        self.right_bord_list =[]
        self.right_bord()
        self.r_head=self.right_bord_list[0]

    def right_bord(self):
        for segment in RIGHT_SEGMENT_LOCATION:
            tonny = Turtle(shape='square')
            tonny.penup()
            tonny.color('white')
            tonny.shapesize(stretch_wid=5,stretch_len=1)
            tonny.speed('fastest')
            tonny.goto(segment)
            self.right_bord_list.append(tonny)

    def up_movement(self):
        for moves in range(len(self.right_bord_list)-1,0,-1):
            x_ax=self.right_bord_list[moves-1].xcor()
            y_ax=self.right_bord_list[moves-1].ycor()
            self.right_bord_list[moves].goto(x_ax,y_ax)

        if self.r_head.ycor()<250:
            self.r_head.setheading(90)
        elif self.r_head.ycor()>-250:
            self.r_head.setheading(270)
        self.r_head.forward(MOVE_DISTANCE)

    # def down_movement(self):
    #     # self.right_bord_list=self.right_bord_list[::-1]
    #     for moves in range(len(self.right_bord_list)-1,0,-1):
    #         x_ax=self.right_bord_list[moves-1].xcor()
    #         y_ax=self.right_bord_list[moves-1].ycor()
    #         self.right_bord_list[moves].goto(x_ax,y_ax)
    #     self.r_head.setheading(270)
    #     self.r_head.forward(MOVE_DISTANCE)

class UserBord:
    def __init__(self):
        self.left_bord_list = []
        self.left_bord()
        self.l_head = self.left_bord_list[0]

    def left_bord(self):
        for segment in LEFT_SEGMENT_LOCATION:
            tonny = Turtle(shape='square')
            tonny.penup()
            tonny.color('white')
            tonny.speed('fastest')
            tonny.goto(segment)
            # tonny.forward()
            self.left_bord_list.append(tonny)

    def movement_user(self):
        for moves in range(len(self.left_bord_list)-1,0,-1):
            x_ax=self.l_head[moves-1].xcor()
            y_ax=self.l_head[moves-1].ycor()
            self.left_bord_list[moves].goto(x_ax,y_ax)

    def up_move(self):
        self.movement_user()
        self.l_head.setheading(90)
        self.l_head.forward(MOVE_DISTANCE)

    def down_move(self):
        self.movement_user()
        self.l_head.setheading(270)
        self.l_head.forward(MOVE_DISTANCE)





            # print(moves)

# li=['a','b','c']
# print(li[::-1])
# a=range(len(li)-1,0,-1)
# a1=range(7,0,-1)
# for i in a:
#     print(i)

# for a in range(len(li)-1,0,-1):
    # print(a)
    # print(f'axis {li[a-1]}')
    # print(a)