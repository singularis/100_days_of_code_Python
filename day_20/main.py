from turtle import Screen
from snake import Snake
import time

display_width = 600
display_height = 600
snake_size = 20
game_speed = 0.1

screen = Screen()
screen.setup(width=display_width, height=display_height)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake(snake_size)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game = True
while is_game:
    screen.update()
    snake.move()
    time.sleep(game_speed)


screen.exitonclick()
