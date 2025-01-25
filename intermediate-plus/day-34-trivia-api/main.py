"""Trivia Game.

This script initializes and runs the trivia game. It fetches questions from the API, processes them
into a usable format, and uses the QuizBrain and QuizInterface classes to manage the game logic and
user interface.

Modules:
--------
- data: Handles fetching questions from the Trivia API.
- question_model: Defines the Question class for handling individual questions.
- quiz_brain: Manages quiz logic, including scoring and question flow.
- ui: Handles the user interface for the quiz game.

Example:
-------
Run this script to start the trivia game. The game fetches questions, initializes the quiz logic,
and launches the GUI for the user to play.

"""

from data import get_questions
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_data = get_questions()

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

