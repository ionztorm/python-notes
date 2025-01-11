"""Food associated class and functionality to be used in Snake game."""

import random
from turtle import Turtle


class Food(Turtle):
    """Food class."""

    def __init__(self) -> None:
        """Initialise the food class."""
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # half the size of default
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        """Position the food in a random locaion."""
        random_x = random.randint(-280, 280)  # noqa: S311
        random_y = random.randint(-280, 280)  # noqa: S311
        self.goto(random_x, random_y)

