import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.penup()
car_manager.goto(500,500)
scoreboeard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    # increase level and car speed
    if player.is_at_finished_line()==True:
        player.move_back()
        car_manager.increase_car_speed()
        scoreboeard.next_level()

     # Detect collision with cars
    for car in car_manager.cars:
         if player.distance(car) < 20:
             scoreboeard.game_over()
             game_is_on=False

screen.exitonclick()