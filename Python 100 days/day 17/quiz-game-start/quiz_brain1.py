
from main import question_bank


class QuizBrains:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list

    def user_question(self):
        current_question=self.question_list[self.question_number]
        ans=input(f'{current_question}')
        # print(ans)
        # return ans


def test():
    print('welcome')