from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

import time

screen_width = 600
screen_height = 600
paddl_width = 5
game_speed = 0.02
paddl_width_full = paddl_width * 20

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle_r = Paddle(screen_width, screen_height, paddl_width, position="right")
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

paddle_l = Paddle(screen_width, screen_height, paddl_width, position="left")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

ball = Ball(screen_width, screen_height, paddle_l, paddle_r)

is_game = True

while is_game:
    screen.update()
    ball.move()
    x_cor = ball.xcor()
    if abs(x_cor) > screen_width / 2 - 20:
        if ball.distance(paddle_r) < 50 or ball.distance(paddle_l) < 50:
            ball.bam()
            if game_speed > 0:
                game_speed -= 0.005
        else:
            ball.game_over(x_cor)
            paddle_l.reset()
            paddle_r.reset()
            time.sleep(2)
            ball.clear()

    time.sleep(game_speed)

screen.exitonclick()
