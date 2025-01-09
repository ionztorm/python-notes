"""A turtle race game using the turtle package."""

import secrets
import turtle as t

colors = ["red", "yellow", "pink", "green", "orange", "purple", "blue"]

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Place your bet!", prompt="Which colour do you think will win?"
)

race_active = False
spacing = 50
first_y_position = -(len(colors) // 2) * spacing
turtles = {}

for color in colors:
    turtles[color] = t.Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(-230, first_y_position)
    first_y_position += spacing

turtles_list = list(turtles.values())

if user_bet:
    race_active = True

while race_active:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_active = False
            if winning_color == user_bet:
                print(f"Congratulations! You choise {user_bet} and won!")
            else:
                print(
                    f"Unlucky, you chose {user_bet}, and lost! The {winning_color} won."
                )
        random_distance = secrets.randbelow(11)
        turtle.forward(random_distance)

screen.exitonclick()
