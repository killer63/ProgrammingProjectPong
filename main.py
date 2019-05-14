# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

from turtle import Screen
import threading
from paddle import Paddle
from pen import Pen
from ball import Ball
from block import Block
from input import Input

# Setup the game window
wn = Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.window_height()
wn.listen()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = Paddle('left')

# Paddle B
paddle_b = Paddle('right')

# Pen
scoreboard = Pen()

# Keyboard bindings
input_a = Input('w', 's', paddle_a, wn)
input_b = Input('Up', 'Down', paddle_b, wn)

# Block
block = Block()

# Ball
ball = Ball(scoreboard, block, paddle_a, paddle_b)

while True:
    threading.Thread(target=input_a.run(), args=()).start()
    threading.Thread(target=input_b.run(), args=()).start()
    threading.Thread(target=ball.move(), args=()).start()
    threading.Thread(target=ball.borders(), args=()).start()
    threading.Thread(target=ball.collision(), args=()).start()
    threading.Thread(target=block.move(), args=()).start()
    wn.update()
