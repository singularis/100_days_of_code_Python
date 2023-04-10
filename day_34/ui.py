from tkinter import *
from quiz_brain import QuizBrain

FONT_NAME = "Arial"

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(font=(FONT_NAME, 12, "italic"), text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.card = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.card_question_text = self.card.create_text(150, 125, width=280, fill="black",
                                                        font=(FONT_NAME, 12, "italic"))
        self.card.grid(column=0, row=1, columnspan=2, pady=20)
        self.decline_image = PhotoImage(file="./images/false.png")
        self.decline_button = Button(image=self.decline_image, highlightthickness=0, command=self.check_answer_false)
        self.decline_button.grid(column=0, row=2, pady=20)
        self.right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.check_answer_true)
        self.right_button.grid(column=1, row=2, pady=20)
        self.get_next_question()
        self.windows.mainloop()

    def get_next_question(self):
        self.card.configure(bg="WHITE")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.card.itemconfigure(self.card_question_text, text=q_text)
        else:
            self.card.itemconfigure(self.card_question_text,
                                    text=f" You have finished with score: {self.quiz.score}/"
                                         f"{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.decline_button.config(state="disabled")

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.card.configure(bg="GREEN")
        else:
            self.card.configure(bg="RED")
        self.windows.after(1000, self.get_next_question)
