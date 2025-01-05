import random
import os
from art import logo

DIFFICULTIES = {"easy": 10, "hard": 5}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_input_options(opts):
    """Return a formatted string of input options. Accepts a list of options."""
    if not opts:
        return "No difficulty options available."

    formatted_options = ", ".join(f"'{opt}'" for opt in opts[:-1])
    if len(opts) > 1:
        formatted_options += f" or '{opts[-1]}'"
    else:
        formatted_options = f"'{opts[0]}'"

    return f"Enter {formatted_options}"


def check_answer(user_guess, correct_number):
    """Check if the user's guess is correct. Returns a boolean indicating if the user has won."""
    has_won = False
    if user_guess == correct_number:
        print(f"\nYou got it! The number was {correct_number}.\n")
        has_won = True
    elif user_guess > correct_number:
        print("Too high.")
    else:
        print("Too low.")
    return has_won


def set_difficulty():
    """Get the user's chosen difficulty and return the number of attempts. Returns an the max number of attempts."""
    difficulty_options = get_input_options(list(DIFFICULTIES.keys()))

    difficulty = input(f"Choose a difficulty. {difficulty_options}\n").lower()

    if difficulty not in DIFFICULTIES:
        difficulty = input(
            f"Invalid input. Please try again. {difficulty_options}\n"
        ).lower()

    max_attempts = DIFFICULTIES[difficulty]

    print(
        f"\nYou chose {difficulty}, so you have {max_attempts} attempts to guess the number."
    )
    return max_attempts


def check_restart():
    new_game = input("Would you like to play again? Type 'yes' or 'no': ").lower()
    if new_game == "yes":
        start_game()
    else:
        print("Goodbye!")


def start_game():
    clear()
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.\n")
    number = random.randint(1, 100)
    attempts = set_difficulty()
    guess = 0

    while guess != number:
        guess = int(input("\nMake a guess: \n"))
        user_has_won = check_answer(guess, number)
        if user_has_won:
            break
        attempts -= 1
        print(f"You have {attempts} attempts remaining")
        if attempts == 0:
            print(f"\nYou ran out of attempts. The number was {number}.")
            print("Game over!\n")
            break

    check_restart()


start_game()
