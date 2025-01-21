"""Ball class and logic for pong."""

import random
from turtle import Turtle

BALL_SHAPE = "circle"
BALL_COLOR = "white"

class Ball(Turtle):
    """Ball class for Pong Game."""

    def __init__(self) -> None:
        """Initialise a Pong Game Ball."""
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.move_x = random.randint(5,10)  # noqa: S311
        self.move_y = random.randint(5,10)  # noqa: S311
        self.__move_speed = 0.1

    def move(self) -> None:
        """Move the ball."""
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)


    def bounce_y(self) -> None:
        """Bounce the ball after collision with horizontal surface."""
        self.move_y *= -1

    def bounce_x(self) -> None:
        """Bounce the ball after collission with vertical surface."""
        self.move_x *= -1

    def reset(self) -> None:
        """Reset the ball to the center of the screen."""
        self.goto(0, 0)
        self.bounce_x()
        self.__move_speed = 0.1

    def get_speed(self) -> float:
        """Get the speed of the ball."""
        return self.__move_speed

    def increase_speed(self) -> None:
        """Increase the speed of the ball."""
        self.__move_speed *= 0.9
