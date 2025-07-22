from turtle import Turtle
ALIGNMENT='center'
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.penup()
        self.scores=0
        self.goto(-260,270)
        self.write(f'count{self.scores}',align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.clear()
        self.scores+=1
        self.write(f'count{self.scores}', align=ALIGNMENT, font=FONT)
