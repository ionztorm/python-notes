"""US States Game."""

import turtle
from pathlib import Path

import pandas as pd

guesses = []

screen = turtle.Screen()
screen.title("U.S. States Game")

turtle.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

"""
# print the xy of clicks so we can plot states.
def get_mouse_click_coor(x, y):
    print(x, y)

# event listener for clicks and gets the xy of the click.
turtle.onscreenclick(get_mouse_click_coor)
"""

states_path = Path("./50_states.csv")
data = pd.read_csv(states_path)
states = data.state.to_list()
while len(guesses) < len(states):
    user_answer = str(
            turtle.textinput(
                title=f"{len(guesses)}/{len(states)} Correct States", prompt="Enter a state name: "
                )
            ).title()

    if user_answer == "Exit":
        missing_states = [state for state in states if state not in guesses]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("missing_states.csv")
        break

    if user_answer in states:
        guesses.append(user_answer)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        coords =(data[data.state == user_answer].x.item(), data[data.state == user_answer].y.item())
        state.goto(coords)
        state.write(user_answer, align="center", font=("Arial", 12, "normal"))

# Keeps the screen open
turtle.mainloop()


