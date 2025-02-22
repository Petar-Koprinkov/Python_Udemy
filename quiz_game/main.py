from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    new_question = Question(question=text, correct_answer=answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_questions():
    user_answer = quiz.next_question()
    quiz.check_correctness(user_answer)

print('Nice, you have completed the quiz!')

