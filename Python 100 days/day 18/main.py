import random
from turtle import Turtle,Screen
tonny=Turtle()
import heroes
import villains
# print(heroes.gen())

tonny.shape('turtle')
tonny.color('red')

# for i in range(15):
#
#     tonny.forward(5)
#     tonny.penup()
#     tonny.forward(5)
#     tonny.pendown()
    # tonny.left(90)

# tonny_the_turtle.forward(100)
# tonny_the_turtle.right(90)
# tonny_the_turtle.forward(100)
# tonny_the_turtle.right(90)
# tonny_the_turtle.forward(100)
# tonny_the_turtle.right(90)
# tonny_the_turtle.forward(100)
# for i in range(5):
#     tonny.left(72)
#     tonny.forward(50)


# angel=360/num_side
# count=[]
# for num_side in range(3,8):
#     angel = 360 / num_side
#     print(angel)
#     count.append(angel)
#     for i in count:
#         tonny.left(i)
#         tonny.forward(100)

# tup=['cornflower blue','medium violet red','firebrick','green yellow','crimson','pale violet red','deep sky blue','medium slate blue','tomato','light salmon','pale violet red','saddle brown','medium slate blue']
# # tonny.pencolor(tup)
# # num_side=8
# for num_side in(3,4,5,6,7,8):
#     tonny.color(random.choice(tup))
#     for _ in range(num_side):
#         angle=360/num_side
#
#         tonny.forward(100)
#         tonny.right(angle)
#

direct=[0,90,180,270]
for i in range(50):
    angles = random.choice(direct)
    print(angles)
    tonny.left(angles)
    tonny.forward(10)

screen=Screen()
screen.exitonclick()


