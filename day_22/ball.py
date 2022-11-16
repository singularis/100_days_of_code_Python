import turtle
from scoreboard import ScoreBoard



class Ball(turtle.Turtle):
    def __init__(self, screen_width, screen_height, paddle_r, paddle_l):
        super().__init__()
        self.scoreboard = ScoreBoard(screen_width)
        self.paddle_r = paddle_r
        self.paddle_l = paddle_l
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen_height_2 = screen_height / 2 - 10
        self.screen_width_2 = screen_width / 2 - 20
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(0)

    def bam(self):
        self.setheading(self.heading() - 120)

    def move(self):
        self.forward(5)
        if abs(self.ycor()) > self.screen_height_2:
            self.bam()

    def game_over(self, x_cor):
        self.home()
        if x_cor < 0:
            self.write(f"Right player WIN!!!!", False, align="center", font=('Arial', 24, 'normal'))
            self.scoreboard.score_increase("right")
            self.setheading(0)

        else:
            self.write(f"Left player WIN!!!!", False, align="center", font=('Arial', 24, 'normal'))
            self.scoreboard.score_increase("left")
            self.setheading(180)


