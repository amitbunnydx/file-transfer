import random
from turtle import Turtle

# from main import create_new

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_color=[]
        self.speed = 0.1


    def create_car(self):
        create=random.randint(0,6)
        if create==5:
            new_car=Turtle(shape='square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            random_x=300
            random_y=random.randint(-250,250)
            new_car.goto(random_x,random_y)
            self.all_color.append(new_car)

    def move(self):
        for car in self.all_color:
            car.backward(STARTING_MOVE_DISTANCE)

    def more_speed(self):
        self.speed *= 0.9
        print(self.speed)