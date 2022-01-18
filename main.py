from turtle import Turtle, Screen, textinput
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setup the screen :
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')

screen.tracer(0)

player1_name = textinput('Players names:', 'First player name:')
player2_name = textinput('Players names:', 'Second player name:')

# Creating the components:
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scores = Scoreboard(player1_name, player2_name)

# Control the paddles:
screen.listen()
screen.onkeypress(key='Up', fun=paddle1.move_up)
screen.onkeypress(key='Down', fun=paddle1.move_down)
screen.onkeypress(key='w', fun=paddle2.move_up)
screen.onkeypress(key='s', fun=paddle2.move_down)


# Layout :
layout = Turtle()
layout.goto(0, 300)
layout.color('white')
layout.pensize(5)
layout.hideturtle()
for n in range(1, 61):
    if n % 2 == 0:
        layout.penup()
    else:
        layout.pendown()
    p = layout.position()[1] - 15
    layout.goto(0, p)


def display_scores(name_1, name_2):
    ball.ball_reset()
    ball.bounce_x()
    scores.clear()
    scores.display(name_1, name_2)


game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 320 and ball.distance(paddle1) < 50) or (ball.xcor() < -320 and ball.distance(paddle2) <= 50):
        ball.bounce_x()
        ball.speed *= 0.9
    if ball.xcor() > 380:
        scores.score_2 += 1
        display_scores(player1_name, player2_name)
    if ball.xcor() < -380:
        scores.score_1 += 1
        display_scores(player1_name, player2_name)
    if scores.score_1 == 10 or scores.score_2 == 10:
        scores.winner(player1_name, player2_name)
        game_is_on = False

screen.exitonclick()
