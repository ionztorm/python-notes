from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


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
            if choice in ["off", "report"]:
                return choice
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


def print_report():
    print("\n--------------------")
    coffee_maker.report()
    money_machine.report()
    print("--------------------\n")


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
            if coffee_maker.is_resource_sufficient(
                drink
            ) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


coffee_machine()
