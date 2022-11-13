import turtle
import random

height = 500
width = 500

screen = turtle.Screen()
screen.setup(width=width, height=height)
user_bat = screen.textinput(title="Make your bet", prompt="Who will win: ? ")
players_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while user_bat not in players_colors:
    user_bat = screen.textinput(title="Make your bet", prompt="Wrong color, please choice correct one: ? ")

turtles = []
y_distance = height / (len(players_colors) + 1)
y_pos = height / 2
x_pos = -(width / 2) + 30
for player in players_colors:
    y_pos -= y_distance
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.speed(10)
    new_turtle.color(player)
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=x_pos, y=y_pos)

winner = None
is_game = True
while is_game:
    for turtle in turtles:
        turtle.speed(random.randint(1, 10))
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > -x_pos:
            winner = turtle.pencolor()
            is_game = False

if winner == user_bat:
    print(f"Greate, you are winner. Winner {winner}")
else:
    print(f"Sorry you lost. Winner {winner}")

screen.listen()
screen.exitonclick()
