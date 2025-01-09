"""Exercises completed on day 19 of 100 days of Python."""

# Requirements: W: Forward, S: Backward, A: Counter Clockwise, D: Clockwise, C: Clear canvas and
# return to center

import turtle as t

turtle = t.Turtle()


def move_forwards() -> None:
    """Move the turtle forward 10 units."""
    turtle.forward(10)


def move_backwards() -> None:
    """Move the turtle backwards 10 units."""
    turtle.backward(10)


def turn_left() -> None:
    """Turn the turtle left."""
    turtle.left(10)


def turn_right() -> None:
    """Turn the turtle right."""
    turtle.right(10)


def reset_turtle() -> None:
    """Clear the canvas and reset the turtles position."""
    turtle.penup()
    turtle.home()
    turtle.clear()
    turtle.pendown()


screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_turtle)
screen.exitonclick()
