import random
from turtle import Turtle, Screen

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

UP=90
DOWN=270
LEFT=180
RIGHT=0
COLOR_LIST=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            tonny = Turtle(shape='square')
            tonny.penup()
            tonny.color(random.choice(COLOR_LIST))
            tonny.goto(position)
            self.snake.append(tonny)

    def move_snake(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def extend(self):
        tonny = Turtle(shape='square')
        tonny.penup()
        tonny.goto(self.snake[-1].position())
        tonny.color(random.choice(COLOR_LIST))
        self.snake.append(tonny)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for snake in self.snake:
            snake.goto(10000,10000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        # self.head.goto(STARTING_POSITION[0])


