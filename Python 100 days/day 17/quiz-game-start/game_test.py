
class QuizBrains:

    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score_count=0
    def still_has_questions(self):

        return self.question_number<len( self.question_list)

    def user_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f'Q.{self.question_number}: {current_question.question} (True/False)? ').lower()
        self.compair_ans(user_ans,current_question.correct_answer)

    def compair_ans(self,user_ans, current_ans):
        if user_ans.lower()==current_ans.lower():
            self.score_count+=1
            print('you got right!')
        else:
            print('you got wrong!')
        print(f'your current score is:{self.score_count}/{self.question_number}')
        print(f'the current ans was:{current_ans}')
        print("\n")
        return  self.score_count,self.question_number

