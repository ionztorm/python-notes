from art import logo, vs
from game_data import data
import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def format_account_data(label, account):
    """accepts a label and an account dictionary and returns a formatted string"""
    return f"{label}: {account['name']}, a {account['description']}, from {account['country']}"


def check_answer(a, b, ans):
    """accepts two account dictionaries and a user answer and returns a boolean"""
    correct_answer = "a" if a["follower_count"] > b["follower_count"] else "b"
    return ans == correct_answer


def start_game():
    clear()
    score = 0
    game_over = False
    account_b = random.choice(data)

    print(logo)

    while not game_over:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(format_account_data("Compare A", account_a))
        print(vs)
        print(format_account_data("Against B", account_b))

        while True:
            try:
                answer = input("\nWho has more followers? Type 'A' or 'B': \n").lower()
                if answer not in ["a", "b"]:
                    raise ValueError(
                        "Your answer was not a valid input. Please try again"
                    )
                break
            except ValueError as e:
                print(e)

        clear()
        print(logo)
        answer_is_correct = check_answer(account_a, account_b, answer)
        if answer_is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, you're wrong! Final score: {score}")
            game_over = True


start_game()
