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
quiz.next_question()

