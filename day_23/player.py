from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen_height_2 = screen_height / 2 - 20
        self.penup()
        self.setposition(y=-self.screen_height_2, x=0)
        self.shape("turtle")
        self.color("black")
        self.setheading(90)

    def move_up(self):
        if self.ycor() < self.screen_width / 2:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -self.screen_width / 2:
            self.backward(20)

    def set_to_start(self):
        self.setposition(y=-self.screen_height_2, x=0)
