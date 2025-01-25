"""quiz_module.

This module provides functionality for handling quiz questions and answers.

It defines the `Question` class, which is used to store a question and its correct answer.

Classes:
--------
- `Question`: A class to represent a quiz question with its text and answer.

Usage:
------
You can create a `Question` object by providing the question text and the correct answer.

Example:
    question = Question("What is the capital of France?", "Paris")
    print(question.text)   # Output: What is the capital of France?
    print(question.answer) # Output: Paris

"""

class Question:
    """A class to represent a quiz question.

    Attributes:
    text (str): The question text.
    answer (str): The correct answer to the question.

    """

    def __init__(self, q_text: str, q_answer: str) -> None:
        """Initialise a new Question object with the given question text and answer.

        Args:
            q_text (str): The question text.
            q_answer (str): The correct answer.

        """
        self.text = q_text
        self.answer = q_answer

