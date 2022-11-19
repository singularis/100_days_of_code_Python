import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen_width = 600
screen_height = 600
obstacle_size = 2
game_speed = 0.1
screen_height_2 = screen_height / 2 - 20

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("white")
screen.title("Crossing")
screen.tracer(0)
screen.listen()

player = Player(screen_width, screen_height)
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

cars = CarManager(screen_width, screen_height)

score_board = Scoreboard(screen_height, screen_width)

is_game = True

while is_game:
    screen.update()
    cars.move_cars()
    if time.time_ns() % (10 - score_board.score) == 0:
        cars.cars_create()
    if player.ycor() >= screen_height_2:
        cars.speed_increase()
        player.set_to_start()
        score_board.score_increase()
    for car in cars.cars_objects:
        if abs(player.ycor()) - abs(car.ycor()) < 10:
            if player.distance(car) < 20:
                score_board.game_over()
                is_game = False
    time.sleep(game_speed)

screen.exitonclick()
