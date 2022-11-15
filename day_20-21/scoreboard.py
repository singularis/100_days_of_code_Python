import turtle

SCORE = 0


class ScoreBoard(turtle.Turtle):
    def __init__(self, display_height):
        super().__init__()
        self.display_height = display_height
        self.score = SCORE
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(display_height/2 - 20)
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 12, 'normal'))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", False, align="center", font=('Arial', 24, 'normal'))