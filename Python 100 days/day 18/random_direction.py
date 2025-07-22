from turtle import Turtle,Screen,xcor
import turtle
import random
tonny=Turtle()

# # print(heroes.gen())
# tup=['cornflower blue','medium violet red','firebrick',
#      'green yellow','crimson','pale violet red','deep sky blue',
#      'medium slate blue','tomato','light salmon','pale violet red',
#      'saddle brown']

direct=[0,90,180,270]
tonny.shape('turtle')
tonny.width(10)
tonny.speed(10)
count=100

def random_color():
    r=int(random.randint(1,255))
    g=int(random.randint(1,255))
    b=int(random.randint(1,255))
    return r,g,b
while count>0:
    # tonny.color(random.choice(tup))
    screen = Screen()
    screen.colormode(255)

    tonny.color((random_color()))
    tonny.setheading(random.choice(direct))
    tonny.forward(random.randint(10, 50))


    # for i in range(5):
    #     # angles = random.choice(direct)
    #     # print(angles)
    #     tonny.left(72)
    #     tonny.forward(distanss)
    count -= 1

#

screen.exitonclick()