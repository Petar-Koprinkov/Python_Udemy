class QuizBrain:
    correct_answer = 0

    def __init__(self, question_list):
        self.question_count = 0
        self.question_list = question_list

    def next_question(self):
        while self.question_count < len(self.question_list):
            current_question = self.question_list[self.question_count]
            self.question_count += 1
            user_answer = input(f'Q.{self.question_count} {current_question.question} (True/False)?: ')

            if user_answer.capitalize() != current_question.correct_answer:
                print('You are wrong!')
                print(f'The correct answer was: {current_question.correct_answer}')
            else:
                print('You got it right!')
                print(f'The correct answer was: {user_answer.capitalize()}')
                QuizBrain.correct_answer += 1
            print(f'Your current score is: {self.question_count}/{QuizBrain.correct_answer}.')
