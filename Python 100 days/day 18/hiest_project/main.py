import turtle

import colorgram
from turtle import Turtle,Screen

import random

tonny=Turtle()
tonny.shape('turtle')
# tonny.width(1)
tonny.color('red')
tonny.hideturtle()
picked_color=[(222, 232, 226), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108),
              (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (128, 189, 143), (83, 20, 44),
              (38, 42, 67), (186, 93, 105), (187, 139, 171), (84, 122, 181), (59, 39, 31), (78, 153, 165),
              (88, 157, 91), (195, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (57, 131, 122),
              (217, 176, 188), (220, 182, 167), (166, 207, 165)]


tonny.speed('fastest')
tonny.penup()
a=-200
tonny.goto(-220, a)
screen = Screen()
screen.colormode(255)
for _ in range(10):
    a+=45
    for _ in range(10):
        tonny.pendown()
        tonny.dot(20,random.choice(picked_color))
        tonny.penup()
        tonny.forward(50)
    tonny.penup()
    tonny.goto(-220, a)

tonny.pendown()

# tonny.clear()

screen=Screen()
screen.exitonclick()
