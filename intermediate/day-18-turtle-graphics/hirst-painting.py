"""Draws 'dot-art' using the Turtle package."""
# import colorgram  # noqa: ERA001
# colors = colorgram.extract("spot-painting.jpeg", 30)  # noqa: ERA001
# rgb_colors = []  # noqa: ERA001
# for color in colors:
#     r = color.rgb.r  # noqa: ERA001
#     g = color.rgb.g  # noqa: ERA001
#     b = color.rgb.b  # noqa: ERA001
#     rgb_colors.append((r, g, b))  # noqa: ERA001
# print(rgb_colors)  # noqa: ERA001

import random as r
import turtle as t

t.colormode(255)
turt = t.Turtle()

colors = [
    (227, 154, 81),
    (171, 79, 46),
    (154, 63, 81),
    (134, 188, 170),
    (44, 120, 88),
    (14, 39, 32),
]

dot_size = 20
move_distance = 50
turt.penup()
turt.speed("fastest")
turt.hideturtle()


def arty_farty(dotsize: int, movedistance: int) -> None:
    """Draws dot-art using a Turtle instance.

    Args:
        dotsize (int): The thickness of the dots to draw.
        movedistance (int): How far the turtle should move.

    """
    turt.right(135)
    turt.forward(370)
    turt.setheading(0)
    for _ in range(10):
        for _ in range(10):
            turt.dot(dotsize, r.choice(colors))  # noqa: S311
            turt.forward(movedistance)
        turt.left(90)
        turt.forward(move_distance)
        turt.left(90)
        turt.forward(500)
        turt.setheading(0)


arty_farty(dot_size, move_distance)

screen = t.Screen()
screen.exitonclick()
