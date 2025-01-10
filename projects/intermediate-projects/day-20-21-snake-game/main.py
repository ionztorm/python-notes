"""Classic snake game."""

import time
from turtle import Screen

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



screen.exitonclick()


