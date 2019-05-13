# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import threading
from paddle import Paddle
from functools import partial
from pen import Pen
from time import sleep
from ball import Ball
from block import Block

wn = turtle.Screen()
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

class Input:
    keysPressed = []

    def __init__(self, upkey, downkey, paddle):
        self.upkey = upkey
        self.downkey = downkey
        self.paddle = paddle
        wn.onkeypress(partial(self.handleInputs, self.upkey), self.upkey)
        wn.onkeypress(partial(self.handleInputs, self.downkey), self.downkey)
        wn.onkeyrelease(partial(self.resetInput, self.upkey), self.upkey)
        wn.onkeyrelease(partial(self.resetInput, self.downkey), self.downkey)

    def run(self):
        if Input.keysPressed.count(self.upkey) == 1:
            self.paddle.up()
        elif Input.keysPressed.count(self.downkey) == 1:
            self.paddle.down()

    def handleInputs(self, key):
        if Input.keysPressed.count(key) == 0:
            Input.keysPressed.append(key)

    def resetInput(self, key):
        Input.keysPressed.remove(key)

input_a = Input('w', 's', paddle_a)
input_b = Input('Up', 'Down', paddle_b)

# Block

block = Block()

# Ball

ball = Ball(scoreboard, block, paddle_a, paddle_b)


while True:
    wn.update()
    threading.Thread(target=input_a.run(), args=()).start()
    threading.Thread(target=input_b.run(), args=()).start()
    threading.Thread(target=ball.move(), args=()).start()
    threading.Thread(target=ball.borders(), args=()).start()
    threading.Thread(target=ball.collision(), args=()).start()
    threading.Thread(target=block.move(), args=()).start()
