"""Scoreboard logic for Snake Game."""

from pathlib import Path
from turtle import Turtle

FONT = ("Arial", 16, "normal")
FONT_COLOR = "white"
FONT_ALIGN = "center"

class Scoreboard(Turtle):
    """Scoreboard class."""

    def __init__(self) -> None:
        """Initialize the scoreboard."""
        super().__init__()
        self.high_score_file = Path("high_score.txt")
        self.score = 0
        self.goto(0, 270)
        self.penup()
        self.color(FONT_COLOR)
        self.hideturtle()
        self.high_score = 0
        self.update_scoreboard()


    def update_scoreboard(self) -> None:
        """Update the scoreboard display."""
        self.clear()


        if not self.high_score_file.exists():
            self.high_score_file.write_text("0")
            self.high_score = 0
        else:
            content = self.high_score_file.read_text().strip()
            self.high_score = int(content)

        self.write(
                f"Score: {self.score} High Score: {self.high_score}", align=FONT_ALIGN, font=FONT
                )


    def increase_score(self) -> None:
        """Increase the score by 1."""
        self.score += 1
        self.update_scoreboard()


    def reset(self) -> None:
        """Reset the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_file.write_text(str(self.score))
        self.score = 0
        self.update_scoreboard()


    # def __display_game_status(self, game_is_over: bool = False) -> None:
    #     """Private. Update the scoreboard."""
    #     text = f"Score: {self.score}" if not game_is_over else f"Game Over\nYour score was {self.score}"
    #     self.clear()
    #     self.write(text, align=FONT_ALIGN, font=FONT)

    # def game_over(self) -> None:
    #     """Display game over message."""
    #     self.goto(0,0)
    #     self.__display_game_status(game_is_over=True)
