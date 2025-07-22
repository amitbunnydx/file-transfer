from turtle import Turtle

ALIGNMENT='center'
FONT=("Arial", 19, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(-10,250)
        self.score=0
        with open('score_file.txt','r')as file:
            contents=file.read()
        self.high_score=int(contents)
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f'Count: {self.score} high score:{self.high_score}',align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            print(self.high_score)
            with open('score_file.txt','w')as file:
                file.write(str(self.high_score))

        self.score=0
        self.clear()
        self.write(f'Count: {self.score} high score:{self.high_score}', align=ALIGNMENT, font=FONT)


    def increasing_score(self):
        self.score += 1
        self.refresh_scoreboard()


    # def game_over_display(self):
    #     self.clear()
    #     self.write(f'Count: {self.score}', align=ALIGNMENT, font=FONT)
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER',align=ALIGNMENT, font=("Arial", 25, "normal"))

