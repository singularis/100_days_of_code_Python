from turtle import Turtle

PADDLE_HEIGHT = 1


class Paddle(Turtle):
    def __init__(self, screen_width, screen_height, paddl_width, position):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.paddl_width = paddl_width
        self.y_pos = 0
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(paddl_width, PADDLE_HEIGHT)
        if position == "right":
            self.x_pos = self.screen_width/2 - 10
        if position == "left":
            self.x_pos = -self.screen_width / 2 + 10
        self.setposition(self.x_pos, 0)

    def move_up(self):
        if self.y_pos < self.screen_width/2 - self.paddl_width*15:
            self.y_pos += 20
            self.goto(self.x_pos, self.y_pos)

    def move_down(self):
        if self.y_pos > -self.screen_width/2 + self.paddl_width*15:
            self.y_pos -= 20
            self.goto(self.x_pos, self.y_pos)

    def paddle_rest(self):
        self.y_pos()




