import random
import time
from turtle import Turtle
from random import randrange, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, screen_width, screen_height):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen_greed = screen_height / 10
        self.speed = STARTING_MOVE_DISTANCE
        self.cars_objects = []

    def cars_create(self):
        rand_position = self.screen_height / 2 - randrange(40, self.screen_height - 40, 20)
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.shapesize(stretch_len=2)
        turtle.setx(self.screen_width / 2)
        turtle.sety(rand_position)
        turtle.color(choice(COLORS))
        self.cars_objects.append(turtle)

    def move_cars(self):
        for car in self.cars_objects:
            car.backward(distance=self.speed)

    def speed_increase(self):
        self.speed += MOVE_INCREMENT
