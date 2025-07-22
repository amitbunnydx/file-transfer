from data import question_data
from question_model import Questions
from game_test import QuizBrains

question_bank = []

for values in question_data:
    question_bank.append(Questions(values['question'], values['correct_answer']))

quiz = QuizBrains(question_bank)

# status = next_question.still_has_questions()
while quiz.still_has_questions():
    quiz.user_question()
    print(f'status is {quiz.still_has_questions()}')

print('congratulation you completed the quiz')

score = quiz.score_count
out_off = quiz.question_number

print(f'your final score was:{score}/{out_off}')
