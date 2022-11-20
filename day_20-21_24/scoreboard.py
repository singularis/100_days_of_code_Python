import turtle
import os

SCORE = 0


class ScoreBoard(turtle.Turtle):
    def __init__(self, display_height):
        super().__init__()
        self.display_height = display_height
        self.score = SCORE
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(display_height / 2 - 20)
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 12, 'normal'))
        self.score_read()
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center",
                   font=('Arial', 12, 'normal'))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score_write()
        self.score = 0
        self.update_scoreboard()

    def score_read(self):
        with open("data.txt") as score_date:
            if os.stat("data.txt").st_size == 0:
                self.score_write()
            else:
                self.high_score = int(score_date.read())

    def score_write(self):
        with open("data.txt", mode="w") as score_data:
            score_data.write(str(self.high_score))

