from turtle import Turtle
import time

class Paddle:
    x = 0
    y = 0
    nOfPaddles = 0

    def __init__(self, alignment):
        self.paddle = Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.penup()
        switcher = {
            'left': -350,
            'center': 0,
            'right': 350
        }
        self.x = switcher[alignment]
        self.paddle.goto(self.x, 0)
        Paddle.nOfPaddles += 1
        self.name = 'Paddle ' + str(Paddle.nOfPaddles)
    
    def up(self):
            if self.y + 70 < 300:
                self.y += 2
                self.paddle.sety(self.y)
            else:
                self.y = 300 - 50
                self.paddle.sety(self.y)
        

    def down(self):
            if self.y - 70 > -300:
                self.y -= 2
                self.paddle.sety(self.y)
            else:
                self.y = -300 + 50
                self.paddle.sety(self.y)

    def gety(self):
        return self.y

    def getx(self):
        return self.x

    def getname(self):
        return self.name