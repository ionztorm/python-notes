"""Fetch and process questions from the Open Trivia Database API."""

import html

import requests

NUM_QUESTIONS = 10
QUESTION_TYPE = "boolean"
TRIVIA_API = "https://opentdb.com/api.php"


def format_questions(questions: list[dict]) -> list[dict]:
    """Unescape HTML entities in question text.

    Args:
        questions (list[dict]): A list of question dictionaries from the API.

    Returns:
        list[dict]: The formatted questions with unescaped HTML entities.

    """
    for question in questions:
        if "question" in question:
            question["question"] = html.unescape(question["question"])
    return questions


def get_questions() -> list[dict]:
    """Fetch new questions from the Open Trivia Database API.

    Returns:
        list[dict]: A list of question dictionaries from the API.

    """
    response = requests.get(
        TRIVIA_API,
        params={"amount": NUM_QUESTIONS, "type": QUESTION_TYPE},
        timeout=10,
    )
    response.raise_for_status()
    return format_questions(response.json()["results"])

