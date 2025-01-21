"""Classic snake game."""

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"
SCREEN_TITLE = "Snake Game"

game_is_active = True

screen = Screen()
screen.tracer(0)
screen.title(SCREEN_TITLE)
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BG_COLOR)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_active:
    screen.update()
    time.sleep(0.06)
    snake.move()

    # Detect collision wih food.
    # Distance method returns the distance of the snake to provided x, y coordinates.
    # Also accepts another turtle instance.
    distance_from_food = snake.head.distance(food)
    if distance_from_food < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with walls.
    if (
            snake.head.xcor() > 290
            or snake.head.xcor() < -290
            or snake.head.ycor() > 290
            or snake.head.ycor() < -290
        ):
        # game_is_active = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 and segment != snake.head:
            # game_is_active = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()



screen.exitonclick()


