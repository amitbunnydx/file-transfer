from turtle import Turtle,Screen

tonny=Turtle()
screen=Screen()

tonny.shape('turtle')

def forward_direction():
    tonny.forward(10)
def backward_direction():
    tonny.backward(10)
def counterclock_direction():
    new_heading=tonny.heading()+10
    tonny.setheading(new_heading)

def clock_direction():
    new_heading = tonny.heading() - 10
    tonny.setheading(new_heading)
    # tonny.goto(10, 0)
def clear_all():
    tonny.clear()
    tonny.penup()
    tonny.home()

screen.listen()
screen.onkey(forward_direction,'w')
screen.onkey(backward_direction,'s')
screen.onkey(counterclock_direction,'a')
screen.onkey(clock_direction,'d')
screen.onkey(clear_all,'c')
screen.exitonclick()