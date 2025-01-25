"""User interface for the quiz application."""

import tkinter as tk
from pathlib import Path

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_IMAGE_FILE = Path("./images/true.png")
FALSE_IMAGE_FILE = Path("./images/false.png")


class QuizInterface:
    """A class for managing the quiz user interface."""

    def __init__(self, quiz: QuizBrain) -> None:
        """Initialize the QuizInterface with the provided quiz logic.

        Args:
            quiz (QuizBrain): The logic handling quiz questions and answers.

        """
        self.quiz = quiz

        # window setup
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # score text
        self.score = 0
        self.score_label = tk.Label(bg=THEME_COLOR, text=f"Score {0}", fg="white")

        # canvas setup
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR, text="Test"
        )

        # buttons setup
        self.true_image = tk.PhotoImage(file=TRUE_IMAGE_FILE)
        self.false_image = tk.PhotoImage(file=FALSE_IMAGE_FILE)
        self.true_button = tk.Button(
            image=self.true_image, highlightthickness=0, command=lambda: self.check_answer("true")
        )
        self.false_button = tk.Button(
            image=self.false_image, highlightthickness=0, command=lambda: self.check_answer("false")
        )

        # initialize UI
        self.place_widgets()
        self.get_next_question()
        self.window.mainloop()

    def place_widgets(self) -> None:
        """Place the widgets in the window using a grid layout."""
        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

    def get_next_question(self) -> None:
        """Display the next question on the canvas."""
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You're out of questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, user_answer: str) -> None:
        """Check the user's answer and update UI accordingly.

        Args:
            user_answer (str): The user's selected answer ("true" or "false").

        """
        answer_is_correct = self.quiz.check_answer(user_answer)
        self.update_score() if answer_is_correct else None
        self.give_visual_feedback(answer_is_correct)
        self.window.after(1000, self.get_next_question)

    def update_score(self) -> None:
        """Update the score displayed on the UI."""
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_visual_feedback(self, answer_is_correct: bool) -> None:
        """Provide visual feedback for the user's answer.

        Args:
            answer_is_correct (bool): True if the answer is correct, otherwise False.

        """
        color = "green" if answer_is_correct else "red"
        self.set_canvas(color)

    def set_canvas(self, color: str = "white") -> None:
        """Set the canvas background color.

        Args:
            color (str, optional): The color to set the canvas background. Defaults to "white".

        """
        self.canvas.config(bg=color)
        if color != "white":
            self.window.after(1000, self.set_canvas)

