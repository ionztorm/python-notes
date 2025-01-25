"""quiz_module.

This module defines the `QuizBrain` class for quiz management.

The `QuizBrain` class is used to manage the quiz logic, track the score, and handle the flow of
questions.

Classes:
--------
- `QuizBrain`: A class to manage quiz functionality, including question progression and score
  tracking.

Usage:
------
Create a `QuizBrain` object by passing a list of `Question` objects.

Example:
    question1 = Question("What is the capital of France?", "Paris")
    question2 = Question("What is 2 + 2?", "4")
    quiz = QuizBrain([question1, question2])

    print(quiz.next_question())  # Output: Q.1: What is the capital of France?
    print(quiz.check_answer("Paris"))  # Output: True

"""

from question_model import Question


class QuizBrain:
    """A class to manage the quiz functionality.

    Includes tracking the score and handling question flow.
    """

    def __init__(self, q_list: list[Question]) -> None:
        """Construct an instance of QuizBrain.

        Args:
            q_list (list[Question]): A list of `Question` objects to be used in the quiz.

        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """Check if there are remaining questions in the quiz.

        Returns:
            bool: True if there are more questions, otherwise False.

        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Get the next question in the quiz.

        Returns:
            str: The next question formatted with its number.

        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def check_answer(self, user_answer: str) -> bool:
        """Check the answer and update the score.

        Args:
            user_answer (str): The user's answer to the current question.

        Returns:
            bool: True if the answer is correct, otherwise False.

        """
        if self.current_question:
            correct_answer = self.current_question.answer
        outcome = user_answer.lower() == correct_answer.lower()
        self.score += outcome
        return outcome

