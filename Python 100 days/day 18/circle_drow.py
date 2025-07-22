import random
from turtle import Turtle,Screen


tonny=Turtle()
tonny.shape('turtle')

screen = Screen()
screen.colormode(255)
tonny.speed(0)
def random_color():
    r=int(random.randint(0,255))
    g=int(random.randint(0,255))
    b=int(random.randint(0,255))
    return r,g,b

def drow_full_circle(length_gap):
    for _ in range(int(360/length_gap)):
        tonny.color((random_color()))
        tonny.circle(100)
        tonny.setheading(tonny.heading()+length_gap)
        # tonny.right(5)
drow_full_circle(10)

screen.exitonclick()