import turtle
import pandas as pd
import time

display_width = 750
display_height = 550
screen = turtle.Screen()
screen.title("Cities")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.setup(width=display_width, height=display_height)
data = pd.read_csv("50_states.csv")
states = data["state"]
turtle.penup()
answered = []
all_state = data.state.to_list()
i = 0

while i < 50:
    answer_state = screen.textinput(title=f"{i}/50 States correct", prompt="Type name here").title()
    if answer_state in answered:
        answered_popup = turtle.Turtle()
        answered_popup.hideturtle()
        answered_popup.penup()
        answered_popup.goto(0, 0)
        answered_popup.write('Already tried', True, align="center", font=('Arial', 25, 'normal'))
        time.sleep(1)
        answered_popup.write("")
        screen.update()
        pass
    if answer_state == "Exit":
        break
    if answer_state in data["state"].values:
        x_cor = (data[data.state == answer_state].x.values[0])
        y_cor = (data[data.state == answer_state].y.values[0])
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x_cor, y_cor)
        state.write(answer_state, True, align="center")
        answered.append(answer_state)
        i = + 1

to_learn = set(all_state) - set(answer_state)
to_learn = pd.DataFrame(to_learn, columns=["States to learn"])
to_learn.to_csv("to_learn.csv", index=False)
print(to_learn)
screen.exitonclick()
