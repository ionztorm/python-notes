"""Scoreboard logic for Snake Game."""

from turtle import Turtle

FONT = ("Arial", 16, "normal")
FONT_COLOR = "white"
FONT_ALIGN = "center"

class Scoreboard(Turtle):
    """Scoreboard class."""

    def __init__(self) -> None:
        """Initialize the scoreboard."""
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.penup()
        self.color(FONT_COLOR)
        self.hideturtle()
        self.__display_game_status()

    def __display_game_status(self, game_is_over: bool = False) -> None:
        """Private. Update the scoreboard."""
        text = f"Score: {self.score}" if not game_is_over else f"Game Over\nYour score was {self.score}"
        self.clear()
        self.write(text, align=FONT_ALIGN, font=FONT)

    def increase_score(self) -> None:
        """Increase the score by 1."""
        self.score += 1
        self.__display_game_status()


    def game_over(self) -> None:
        """Display game over message."""
        self.goto(0,0)
        self.__display_game_status(game_is_over=True)


