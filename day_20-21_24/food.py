from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, display_width, display_height, snake_size):
        super().__init__()
        self.display_width = display_width
        self.display_height = display_height
        self.snake_size = snake_size
        self.shape("circle")
        self.penup()
        self.width(self.snake_size)
        self.color("blue")
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        random_x = random.randint(0, ((self.display_width / 2) - self.snake_size))
        random_y = random.randint(0, ((self.display_height / 2) - self.snake_size))
        self.goto(random_x, random_y)
