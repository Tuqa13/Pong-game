from turtle import Turtle
import random

MOVE_DISTANCE = 10
Y_COR_SPACE = [280, -280]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.left(random.randint(-45, 45))
        self.x_distance = 10
        self.y_distance = 10
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_distance
        new_y = self.ycor() + self.y_distance
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_distance *= -1

    def bounce_y(self):
        self.y_distance *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.speed = 0.1
