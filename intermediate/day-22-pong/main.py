"""Classic Pong Game."""

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "Pong Game"

game_is_on = True
sleep_time = 0.1


screen = Screen()
screen.listen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

# instatiations
scoreboard = Scoreboard()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.update()

# movement event listeners
screen.onkey(left_paddle.go_up, "Left")
screen.onkey(left_paddle.go_down, "Right")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")


while game_is_on:
    time.sleep(ball.get_speed())
    screen.update()
    ball.move()

    # Detect Top and Bottom Wall Collision

    if ball.ycor() >= 288 or ball.ycor() <= -288:
        ball.bounce_y()

    # detect ball collision paddles
    if (
            (right_paddle.xcor() - 12 <= ball.xcor() + 10 <= right_paddle.xcor() + 10)
            and (ball.distance(right_paddle) <= 63)
            and ball.move_x > 0
        ) or (
            (left_paddle.xcor() + 12 >= ball.xcor() - 10 >= left_paddle.xcor() - 10)
            and (ball.distance(left_paddle) <= 63)
            and ball.move_x < 0
        ):
        ball.increase_speed()
        ball.bounce_x()

    if ball.xcor() >= 388:
        scoreboard.update_scores("left")
        ball.reset()
    elif ball.xcor() <= -388:
        scoreboard.update_scores("right")
        ball.reset()

screen.exitonclick()
