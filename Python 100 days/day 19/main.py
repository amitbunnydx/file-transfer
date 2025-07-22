from turtle import Turtle,Screen

tonny=Turtle()
screen=Screen()



def key_function():
    tonny.forward(10)

screen.listen()
screen.onkey(key_function,'space')
screen.exitonclick()


