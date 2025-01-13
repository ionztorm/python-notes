"""Main turtle crossing game entry point."""

import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

EASY = 0.9
MEDIUM = 0.5
HARD = 0.2
GODLY = 0.1

difficulty = GODLY

sleep_time = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect collision with car.
    cars = car_manager.cars
    for car in cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect player success
    if player.ycor() >= 280:
        player.reset()
        scoreboard.increase_score()
        sleep_time *= difficulty
        # Move distance eventually > width of car. Jumps right over turtle.
        # car_manager.increase_speed()

screen.exitonclick()
