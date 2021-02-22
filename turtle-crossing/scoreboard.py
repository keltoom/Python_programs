from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.level = 1
        self.write(f'Level:{self.level}', align='center', font=FONT)
        self.next_level()

    def next_level(self):
        self.clear()
        self.write(f'Level:{self.level}', align='center', font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)
