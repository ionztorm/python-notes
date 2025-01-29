"""Workout tracker."""

import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
NUTRITIONIX_API = "https://trackapi.nutritionix.com"
NUTRITIONIX_EXERCISE_ENDPOINT = f"{NUTRITIONIX_API}/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/e5ab60d36aab0e2fada4e1e132a5c2c9/myWorkouts/workouts"
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

NOT_IMPLEMENTED_MESSAGE = "Not implemented yet."


if not all([NUTRITIONIX_APP_ID, NUTRITIONIX_APP_KEY, SHEETY_BEARER_TOKEN]):
    raise ValueError("Please ensure you have set the environment variables.")

nutiionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}


def main_menu() -> str:
    """Display the main menu."""
    print("What would you like to do?\n")
    print("1. Log workout")
    print("2. Get workouts")
    print("3. Update workout")
    print("4. Delete workout")
    print("5. Exit")
    return input("\nEnter your choice: ")


def log_workout() -> dict:
    """Log a new workout."""
    parameters = {
        "query": input("Tell me which exercise you did:\n"),
        "weight_kg": input("Enter your weight in kg:\n"),
        "height_cm": input("Enter your height in cm:\n"),
        "age": input("Enter your age:\n"),
    }

    response = requests.post(
        url=NUTRITIONIX_EXERCISE_ENDPOINT, json=parameters, headers=nutiionix_headers, timeout=5
    )
    response.raise_for_status()

    return response.json()


def format_workout(workouts: dict) -> dict:
    """Format the workout for Sheety."""
    workout = workouts["exercises"][0]
    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%H:%M:%S")
    return {
        "workout": {
            "date": date,
            "time": time,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }


def save_workout(workout: dict) -> None:
    """Record the workout."""
    sheety_headers = {
        "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=workout, headers=sheety_headers, timeout=5)
    response.raise_for_status()
    print("Workout recorded.")


def main() -> None:
    """Run the program."""
    while True:
        choice = main_menu()

        if choice == "1":
            save_workout(format_workout(log_workout()))
        elif choice == "2":
            print(NOT_IMPLEMENTED_MESSAGE)
        elif choice == "3":
            print(NOT_IMPLEMENTED_MESSAGE)
        elif choice == "4":
            print(NOT_IMPLEMENTED_MESSAGE)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
