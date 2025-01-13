"""Scoreboard class for Turtle Crossing Game."""

from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_ALIGN = "center"
FONT_COLOR = "black"


class Scoreboard(Turtle):
    """Scoreboard class for Turtle Crossing Game."""

    def __init__(self) -> None:
        """Construct a Scoreboard instance."""
        super().__init__()
        self.penup()
        self.color(FONT_COLOR)
        self.goto(0, 260)
        self.level = 1
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self) -> None:
        """Update the scoreboard."""
        self.clear()
        score_string = f"Level: {self.level}"
        self.write(arg=score_string, align=FONT_ALIGN, font=FONT)


    def increase_score(self) -> None:
        """Increase the score by 1."""
        self.level += 1
        self.update_scoreboard()


    def game_over(self) -> None:
        """Display Game Over."""
        self.goto(0,0)
        self.write("GAME OVER!", align=FONT_ALIGN, font=FONT)
        self.goto(0, -30)
        self.write("You got flattened!", align=FONT_ALIGN, font=FONT)

