from turtle import Turtle
import time

FONT = ('Courier', 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self, name_1, name_2):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.display(name_1, name_2)

    def display(self, name_1, name_2):
        self.goto(250, 250)
        self.write(self.score_1, False, 'center', FONT)
        self.goto(-150, 250)
        self.write(self.score_2, False, 'center', FONT)
        self.goto(170, 250)
        self.write(f'{name_1}:', False, 'center', FONT)
        self.goto(-230, 250)
        self.write(f'{name_2}:', False, 'center', FONT)

    def winner(self, name_1, name_2):
        self.goto(0, 0)
        self.color('red')
        self.write('Game Over!', False, 'center', ('Courier', 50, 'bold'))
        time.sleep(1.5)
        self.clear()
        if self.score_1 == 10:
            self.write(f'The winner is {name_1}\n Congratulations', False, 'center', FONT)
        else:
            self.write(f'The winner is {name_2}\nCongratulations', False, 'center', FONT)
