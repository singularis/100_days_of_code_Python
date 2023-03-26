from tkinter import *
from random import choice
import pandas as pd
import threading

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

timer = 0


def next_world(remember=False):
    def background_change():
        card.itemconfigure(card_image, image=card_back_img)
        card.itemconfigure(card_language_text, text="English")
        card.itemconfigure(world_to_guess, text=random_world['English'])

    global timer
    timer = threading.Timer(3, background_change)
    if timer.is_alive():
        timer.cancel()
    card.itemconfigure(card_image, image=card_front_img)
    card.itemconfigure(card_language_text, text="Polish")
    random_world = choice(worlds_dict)
    while random_world['Remember'] == True:
        print(random_world['Remember'])
        random_world = choice(worlds_dict)
    if remember:
        data.loc[data['Polish'] == random_world['Polish'], 'Remember'] = 'True'
        data.to_csv("./data/test.csv", index=False)
    card.itemconfigure(world_to_guess, text=random_world['Polish'])
    timer.start()


window = Tk()
window.title("Flashy")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_image = card.create_image(400, 263, image=card_front_img)
card_language_text = card.create_text(400, 150, text="Polish", fill="black", font='Arial 40 italic')
world_to_guess = card.create_text(400, 263, text="English", fill="black", font='Arial 60 italic')
card.grid(column=0, row=0, columnspan=2)

decline_image = PhotoImage(file="./images/wrong.png")
decline_button = Button(image=decline_image, highlightthickness=0, command=lambda: next_world(remember=False))
decline_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda: next_world(remember=True))
right_button.grid(column=1, row=1)

if __name__ == "__main__":
    data = pd.read_csv("./data/test.csv")
    worlds_dict = data.to_dict(orient="records")
    next_world()
    window.mainloop()
