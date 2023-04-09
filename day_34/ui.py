from tkinter import *

FONT_NAME = "Arial"

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(font=(FONT_NAME, 12, "italic"), text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.card = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.card_question_text = self.card.create_text(150, 125, text="Polish", fill="black",
                                                        font=(FONT_NAME, 20, "italic"))
        self.card.grid(column=0, row=1, columnspan=2, pady=20)
        self.decline_image = PhotoImage(file="./images/false.png")
        self.decline_button = Button(image=self.decline_image, highlightthickness=0)
        self.decline_button.grid(column=0, row=2, pady=20)
        self.right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0)
        self.right_button.grid(column=1, row=2, pady=20)
        self.windows.mainloop()
