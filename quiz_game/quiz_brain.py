class QuizBrain:
    score = 0

    def __init__(self, question_list):
        self.question_count = 0
        self.question_list = question_list

    def still_questions(self):
        return self.question_count < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_count]
        self.question_count += 1
        return input(f'Q.{self.question_count} {current_question.question} (True/False)?: ')

    def check_correctness(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_count - 1].correct_answer.lower():
            print('You got it right!')
            QuizBrain.score += 1
        else:
            print('That\'s wrong!')

        print(f'The correct answer was: {self.question_list[self.question_count - 1].correct_answer}')
        print(f'Your current score is: {QuizBrain.score}/{self.question_count}')

