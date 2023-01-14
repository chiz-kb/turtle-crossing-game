from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.pu()
        self.goto(0,260)
        self.score()

    def score(self):
        self.clear()
        self.write(arg=f'level:{self.level}',align='center',font=FONT)

    def update_level(self):
        self.level+=1
        self.score()
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f'Game Over',align='center',font=FONT)