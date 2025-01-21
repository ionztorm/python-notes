"""Paddle class and logic for pong."""

from turtle import Turtle

PADDLE_COLOR = "white"

class Paddle(Turtle):
    """Paddle class for Pong Game."""

    def __init__(self, position: tuple) -> None:
        """Initialise a Pong Game Paddle."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self) -> None:
        """Move paddle upward."""
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self) -> None:
        """Move paddle downward."""
        self.goto(self.xcor(), self.ycor() - 20)
