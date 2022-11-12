class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.run_out_questions = True
        self.question_list = question_list
        self.score = 0

    def still_has_question(self, user_answer):
        correct_answer = self.question_list[self.question_number - 1].answer
        if user_answer == correct_answer:
            self.score += 1
            print(f'''You got it right!
The correct answer was {correct_answer}
Your score {self.score}/{self.question_number}''')
            return True
        else:
            print("No luck, keep trying")
            return False

    def next_question(self):
        if self.question_number == len(self.question_list):
            self.run_out_questions = False
        else:
            question_to_ask = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {question_to_ask.text} (True/False)?:")
            return user_answer
