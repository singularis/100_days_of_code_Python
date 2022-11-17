from turtle import Screen
import time

screen_width = 600
screen_height = 600
obstacle_size = 2
game_speed = 0.02

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("white")
screen.title("Crossing")
screen.tracer(0)
screen.listen()



is_game = True

while is_game:
    time.sleep(game_speed)
    pass

screen.exitonclick()