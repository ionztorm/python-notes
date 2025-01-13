"""Car Manager class for car creation and movement in Turtle Crossing game."""

import random
import secrets

from player import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    """Care manager class for car creation and movement in Turtle Crossing game."""

    def __init__(self) -> None:
        """Construct an instance of CarManager."""
        self.cars = []
        self.old_cars = []


    def create_car(self) -> None:
        """Create a car in Turtle Crossing."""
        gamble = secrets.randbelow(7)
        if gamble == 1:
            if self.old_cars:
                car = self.old_cars.pop()
            else:
                car = Turtle("square")
                car.penup()
                car.color(secrets.choice(COLORS))
                car.shapesize(stretch_len=2, stretch_wid=1)
                car.setheading(180)

            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)


    def move(self) -> None:
        """Move the car forward."""
        for car in self.cars:
            if car.xcor() < -320:

                self.old_cars.append(car)
                self.cars.remove(car)
            else:
                car.forward(5)

