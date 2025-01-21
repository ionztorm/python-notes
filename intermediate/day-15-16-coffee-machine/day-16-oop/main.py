import os

from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_choice(options):
    """Displays a menu in the terminal and allows the user to select an option.

    Args:
        options (list): A list of strings representing the options to choose from.

    Returns:
        str: The selected option.
    """
    if not options or not isinstance(options, list):
        raise ValueError("Options must be a list with at least one item.")

    while True:
        print("\nWhat would you like?:")
        print("\n".join(f"{i + 1}. {option}" for i, option in enumerate(options)))
        choice = input("Enter the number of your choice: ").strip()

        if choice in ["off", "report"]:
            return choice

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Invalid choice. Please try again.")


def neat_wrap(func):
    def wrapper():
        print("\n--------------------")
        func()
        print("--------------------\n")

    return wrapper


@neat_wrap
def print_report():
    coffee_maker.report()
    money_machine.report()


def coffee_machine():
    clear()
    making_coffee = True

    while making_coffee:
        options = menu.get_items().rstrip("/").split("/")
        choice = get_choice(options)

        if choice == "report":
            print_report()

        elif choice == "off":
            making_coffee = False
            print("Goodbye!")
            break

        else:
            print(choice)
            drink = menu.find_drink(choice)
            if not drink:
                continue
            if coffee_maker.is_resource_sufficient(
                drink
            ) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


coffee_machine()
coffee_machine()
