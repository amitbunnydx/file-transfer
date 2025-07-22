import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.up,'Up')
screen.onkey(player.down,'Down')


game_is_on = True
while game_is_on:
    time.sleep(car_manager.speed)
    screen.update()
    car_manager.create_car()
    # time.sleep(1)
    car_manager.move()


    for car in car_manager.all_color:
       if car.distance(player)<25:
           print('loos')
           game_is_on =False

    if player.ycor()==280:
        print('complited')
        player.reset()
        car_manager.more_speed()
        scoreboard.update_score()


screen.exitonclick()