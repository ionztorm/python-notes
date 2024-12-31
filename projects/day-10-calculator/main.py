import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2


def clear():
    os.system("cls" if os.name == "nt" else "clear")


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate():
    repeat_new = True
    n1, n2, result = 0.0, 0.0, 0.0
    operation = ""
    more_calculations = ""

    n1 = float(input("What is the first number? \n"))

    while repeat_new:

        for o in operations:
            print(o)

        operation = input("Pick an operation: \n")
        while operation not in operations:
            operation = input("Invalid input. Pick an operation: \n")

        n2 = float(input("What is the second number? \n"))

        result = operations[operation](n1, n2)

        print(f"\n{n1} {operation} {n2} = {result}\n")

        more_calculations = input(
            f"Do you want to do more calculations on {result}? Type 'yes' or 'no' \n"
        ).lower()

        while more_calculations not in ["yes", "no"]:
            more_calculations = input(
                f"Invalid input. Do you want to do more calculations on {result}? Type 'yes' or 'no' \n"
            ).lower()

        if more_calculations == "no":
            clear()
            calculate()
        else:
            n1 = result


calculate()
