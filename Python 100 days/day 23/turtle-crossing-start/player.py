from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('blue')
        self.penup()
        self.new_x=0
        self.new_y=-290
        self.goto(STARTING_POSITION)
        self.left(90)
        self.forward(MOVE_DISTANCE)


    def up(self):
        new_y=self.ycor()+10
        self.goto(self.new_x,new_y)

    def down(self):

        new_y = self.ycor() - 10
        self.goto(self.new_x, new_y)

    def reset(self):
        self.goto(STARTING_POSITION)




