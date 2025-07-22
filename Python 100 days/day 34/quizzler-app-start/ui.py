from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quiz_brain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score=Label(text='Score: 0',fg='white',bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.quote_text = self.canvas.create_text(150, 125, text="Some question text",width=280,fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)


        true_img = PhotoImage(file="images/true.png")
        self.button = Button(image=true_img, highlightthickness=0, command=self.true_press )
        self.button.grid(column=0 ,row=2)

        false_img = PhotoImage(file="images/false.png")
        self.button1 = Button(image=false_img, highlightthickness=0, command=self.false_press )
        self.button1.grid(column=1, row=2)
        self.get_next()

        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text=self.quiz.next_question()
            self.canvas.itemconfigure(self.quote_text,text=q_text)
        else:
            self.canvas.itemconfigure(self.quote_text,text=f'Your rech the end of the questions your score is {self.quiz.score-1}')
            self.button.config(state='disabled')
            self.button1.config(state='disabled')

    def true_press(self):
        self.give_feedback(self.quiz.check_answer('True'))
    def false_press(self):
        result=self.quiz.check_answer('False')
        self.give_feedback(result)
    def give_feedback(self,is_right):
        print(is_right)
        if is_right:
            print('in')
            self.canvas.config(bg='Green')
        else:
            print('in2')
            self.canvas.config(bg='Red')
        self.window.after(500,self.get_next)