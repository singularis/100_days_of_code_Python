import turtle

SCORE_L = 0
SCORE_R = 0


class ScoreBoard(turtle.Turtle):
    def __init__(self, display_height):
        super().__init__()
        self.display_height = display_height
        self.score_l = SCORE_L
        self.score_r = SCORE_R
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(display_height/2 - 20)
        self.write(f"Score left: {self.score_l} Score right: {self.score_r}", False, align="center",
                   font=('Arial', 12, 'normal'))

    def score_increase(self, player):
        self.clear()
        if player == "left":
            self.score_l += 1
        else:
            self.score_r += 1
        self.write(f"Score left: {self.score_l} Score right: {self.score_r}", False, align="center",
                   font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", False, align="center", font=('Arial', 24, 'normal'))