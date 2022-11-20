from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

display_width = 600
display_height = 600
snake_size = 20
game_speed = 0.1
display_width_2 = display_width / 2 - 20
display_height_2 = display_height / 2 - 20

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

food = Food(display_width, display_height, snake_size)
score_board = ScoreBoard(display_height)

is_game = True
while is_game:
    screen.update()
    snake.move()
    time.sleep(game_speed)
    if snake.head.distance(food) < snake_size:
        food.refresh()
        snake.extend()
        score_board.score_increase()
    # Borders collision
    if -display_width_2 < snake.head.xcor() > display_width_2 \
            or -display_height_2 < snake.head.ycor() > display_height_2:
        score_board.reset_scoreboard()
        snake.reset_snake()

    # Head collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
