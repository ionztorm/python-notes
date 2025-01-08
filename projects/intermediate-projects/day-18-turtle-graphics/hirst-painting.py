# import colorgram
#
# colors = colorgram.extract("spot-painting.jpeg", 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
#
# print(rgb_colors)
import turtle as t
import random as r

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


def arty_farty(dotsize, movedistance):
    turt.right(135)
    turt.forward(370)
    turt.setheading(0)
    for _ in range(10):
        for _ in range(10):
            turt.dot(dotsize, r.choice(colors))
            turt.forward(movedistance)
        turt.left(90)
        turt.forward(move_distance)
        turt.left(90)
        turt.forward(500)
        turt.setheading(0)


arty_farty(dot_size, move_distance)

screen = t.Screen()
screen.exitonclick()
