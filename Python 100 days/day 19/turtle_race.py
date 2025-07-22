import random
import turtle
from turtle import Turtle,Screen

tonny=Turtle()
screen=Screen()
screen.setup(800,400)
user_bet=screen.textinput(title='Make your bet', prompt='Which turtle will will the rase ? Enter color: ')
# print(user_bet)
rainbow_color=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet' ]
y_position=[120,80,40,0,-40,-80,-120]
participant_list=[]
for turtle_index in range(6):
    tonny=Turtle(shape='turtle')
    tonny.color(rainbow_color[turtle_index])
    tonny.penup()
    tonny.goto(-350,y_position[turtle_index])
    participant_list.append(tonny)

print(participant_list)
game_on=False

if user_bet:
    game_on=True

while game_on:
    for turtle in participant_list:
        if turtle.xcor()>355:
            print(f'you win {turtle.pencolor()}')
            game_on=False
            if turtle.pencolor()== user_bet:
                print(f'congratulation you win {turtle.pencolor()}')
            else:
                print(f'sorry you loss winning turtle is {turtle.pencolor()}')
        turtle.forward(random.randint(5,20))

# red_t=Turtle(shape='turtle')
# red_t.penup()
# red_t.color(rainbow_color[0])
# red_t.goto(-350,120)
#
# orange_t=Turtle(shape='turtle')
# orange_t.penup()
# orange_t.color(rainbow_color[1])
# orange_t.goto(-350,80)
#
# yellow_t=Turtle(shape='turtle')
# yellow_t.penup()
# yellow_t.color(rainbow_color[2])
# yellow_t.goto(-350,40)
#
# green_t=Turtle(shape='turtle')
# green_t.penup()
# green_t.color(rainbow_color[3])
# green_t.goto(-350,0)
#
# blue_t=Turtle(shape='turtle')
# blue_t.penup()
# blue_t.color(rainbow_color[4])
# blue_t.goto(-350,-40)
#
# indigo_t=Turtle(shape='turtle')
# indigo_t.penup()
# indigo_t.color(rainbow_color[5])
# indigo_t.goto(-350,-80)
#
# violet_t=Turtle(shape='turtle')
# violet_t.penup()
# violet_t.color(rainbow_color[6])
# violet_t.goto(-350,-120)


screen.exitonclick()