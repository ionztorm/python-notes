"""Player class for Turtle Crossing game."""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Player class for Turtle Crossing game."""

    def __init__(self) -> None:
        """Construct an instance of Player."""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self) -> None:
        """Move the turtle forward by 10."""
        self.forward(MOVE_DISTANCE)


    def reset(self) -> None:
        """Reset player back to starting position."""
        self.goto(STARTING_POSITION)
