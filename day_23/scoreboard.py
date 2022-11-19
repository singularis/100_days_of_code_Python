import turtle

FONT = ("Courier", 24, "normal")
SCORE = 0


class Scoreboard(turtle.Turtle):
    def __init__(self, display_height, display_wight):
        super().__init__()
        self.display_height = display_height
        self.display_wight = display_wight
        self.score = SCORE
        self.hideturtle()
        self.color("black")
        self.penup()
        self.sety(display_height / 2 - 30)
        self.setx(- display_wight/2 + 30)
        self.write(f"Level: {self.score}", False, align="left", font=('Courier', 12, 'normal'))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, align="left", font=('Courier', 12, 'normal'))

    def game_over(self):
        self.goto(-70, 0)
        self.write(f"Game over", False, align="left", font=('Courier', 24, 'normal'))
