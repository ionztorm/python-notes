"""Scoreboard class and logic for pong."""

from turtle import Turtle

FONT = ("Courier", 20, "normal")
FONT_COLOR = "white"
FONT_ALIGN = "center"


class Scoreboard(Turtle):
    """Scoreboard class for Pong Game."""

    def __init__(self) -> None:
        """Iniialise the scoreboard."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()


    def update_scoreboard(self) -> None:
        """Use a turtle instance to render a scorboard."""
        scoreboard_text = f"{self.left_score} : {self.right_score}"
        self.clear()
        self.write(scoreboard_text, align=FONT_ALIGN, font=FONT)


    def update_scores(self,side:str) -> None:
        """Update a score.

        Args:
            side (str): The side to update the score.

        """
        if side == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.update_scoreboard()
