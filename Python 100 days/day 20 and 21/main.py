import time
from itertools import count
from turtle import Screen
from food import Food
from snake import Snake
from scorebord import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('the snake game')
screen.tracer(0)  # user to look snake properly It will blank screen

game_s=Snake()
food=Food()
score_data=Scoreboard()

screen.listen()
screen.onkey(game_s.up,"Up")
screen.onkey(game_s.down,"Down")
screen.onkey(game_s.left,"Left")
screen.onkey(game_s.right,"Right")

moving=True
while moving:
    screen.update()  # it will show snake
    time.sleep(0.1)
    game_s.move_snake()

#collision detect with food
    if game_s.head.distance(food)<15:
        food.refresh()
        game_s.extend()
        score_data.increasing_score()

# collision with wall.
    if game_s.head.xcor()>290 or game_s.head.xcor()< -290 or game_s.head.ycor()>290 or game_s.head.ycor()<-290:
        score_data.reset()

        game_s.reset()


#collision with tail
    for extended in game_s.snake[1::]:
        if game_s.head.distance(extended)<10:
            print('collision')
            score_data.reset()

            game_s.reset()







screen.exitonclick()
