class QuizBrain:
    def __init__(self, question_list):
        self.question_count = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_count]
        self.question_count += 1
        user_answer = input(f'Q.{self.question_count} {current_question.question} (True/False)?:  ')

