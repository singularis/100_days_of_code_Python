from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_obj = Question(question["text"], question["answer"])
    question_bank.append(question_obj)

is_on = True
ask_question = QuizBrain(question_bank)
while ask_question.run_out_questions:
    user_answer = ask_question.next_question()
    is_on = ask_question.still_has_question(user_answer)
print(f"Your final result is {ask_question.score}/{ask_question.question_number}")