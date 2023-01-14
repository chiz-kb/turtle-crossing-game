import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
create_car=CarManager()
player=Player()
score_board=Scoreboard()
screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    create_car.car()
    create_car.move()
    for car in create_car.cars:
      if  car.distance(player)<15:
        score_board.game_over()
        game_is_on=False
    if player.ycor()==280:
        player.restart()
        score_board.update_level()
        create_car.speed_up()
screen.exitonclick()
