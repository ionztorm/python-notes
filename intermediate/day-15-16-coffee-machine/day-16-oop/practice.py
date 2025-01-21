"""
https://docs.python.org/3/library/turtle.html
"""

# from turtle import Turtle, Screen

from prettytable import PrettyTable


# leonardo = Turtle()  # create an instance of the Turtle class
# leonardo.shape("turtle")  # change the shape of the turtle to a turtle
# leonardo.color("chartreuse3")
# leonardo.forward(100)
#
#
# my_screen = Screen()  # create an instance of the Screen class
# my_screen.exitonclick()  # close the screen when clicked

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # doesn't appear to work before columns


print(table)
