from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2)
        # self.new_x=
        # self.new_y=
