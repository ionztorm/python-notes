# day 15 project - intermediate

import os

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 3.0,
    },
}
takings = 0


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_choice(options):
    """
    Displays a menu in the terminal and allows the user to select an option.

    Args:
        options (list): A list of strings representing the options to choose from.

    Returns:
        str: The selected option.
    """
    if not options or not isinstance(options, list):
        raise ValueError("Options must be a list with at least one item")

    while True:
        try:
            print("What would you like?:")
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
            choice = input("Enter the number of your choice: ")
            if choice == "off":
                return "off"
            elif choice == "report":
                return "report"
            else:
                choice = int(choice)
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    raise ValueError(
                        "Invalid choice. Please enter a number corresponding to the options above."
                    )
        except ValueError as e:
            print(e)


def print_report(levels):
    """
    Accepts a dictionary of items and their levels and prints a report.
    """
    print("\n-------------------------")
    print("Report:")
    for item, level in levels.items():
        measurement = (
            "ml" if item in ["water", "milk"] else "g" if item == "coffee" else "$"
        )
        print(f"{item.capitalize()}: {level}{measurement}")
    print(f"Money ${takings}")
    print("-------------------------\n")


def check_resources(user_choice):
    """
    Accepts a user choice and checks if there are enough resources to make the drink.
    Outputs a message if there are not enough resources.
    """
    ingredients = MENU[user_choice]["ingredients"]
    for ingredient, amount in ingredients.items():
        if amount > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins(quarters):
    """
    Calculate the total value of coins inserted.
    """

    def with_dimes(dimes):
        def with_nickles(nickles):
            def with_pennies(pennies):
                return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

            return with_pennies

        return with_nickles

    return with_dimes


def make_coffee(user_choice):
    """
    Makes the coffee based on the user's choice.
    """
    global takings
    ingredients = MENU[user_choice]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    takings += MENU[user_choice]["price"]


def transaction(price, paid):
    """
    Accepts the price of the drink and the amount paid by the user as integers.

    Checks if the user has paid enough money and returns the change if they have.

    Prints an appropriate message to the user.
    """
    if paid < price:
        print(f"Sorry, you're ${(price - paid):.2f}. Your payment has been refunded.")
        return False

    change = paid - price

    print(f"\nPayment accepted, thank you.")
    print(f"Please take your ${change:.2f} change")
    print("Thank you for your custom, have a great day ☕️\n")
    return True


def coffee_machine():
    clear()
    placing_order = True

    while placing_order:
        choice = get_choice(list(MENU.keys()))

        if choice == "report":
            print_report(resources)

        elif choice == "off":
            print("Turning off the coffee machine.")
            placing_order = False

        else:
            have_resources = check_resources(choice)
            if not have_resources:
                continue
            drink_price = MENU[choice]["price"]
            print(f"{choice.capitalize()} costs ${drink_price}.\n")
            quarters = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            transaction_is_successful = transaction(
                drink_price, process_coins(quarters)(dime)(nickles)(pennies)
            )
            make_coffee(choice)
            placing_order = False if not transaction_is_successful else True


coffee_machine()
