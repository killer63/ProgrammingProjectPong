from turtle import Turtle
from threading import Lock

lock = Lock()

class Ball:
    global lock

    def __init__(self, scoreboard, block, paddle1, paddle2):
        self.ball = Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.x = 0
        self.y = 0
        self.ball.goto(self.x, self.y)
        self.ball.dx = 1
        self.ball.dy = 1
        self.scoreboard = scoreboard
        self.block = block.block
        self.paddle1 = paddle1
        self.paddle2 = paddle2

    # borders of screen
    def borders(self):
        if self.gety() > 290:
            self.ball.sety(290)
            self.y = 290
            self.ball.dy *= -1

        elif self.gety() < -290:
            self.ball.sety(-290)
            self.y = -290
            self.ball.dy *= -1

        elif self.getx() > 350:
            self.scoreboard.a_win()
            self.ball.goto(0, 0)
            self.x = 0
            self.y = 0
            self.ball.dx *= -1

        elif self.getx() < -350:
            self.scoreboard.b_win()
            self.ball.goto(0, 0)
            self.x = 0
            self.y = 0
            self.ball.dx *= -1

    # move of the ball
    def move(self):
        self.ball.setx(self.getx() + self.ball.dx)
        self.x = self.getx() + self.ball.dx
        self.ball.sety(self.gety() + self.ball.dy)
        self.y = self.gety() + self.ball.dy

    # ball collisions
    def collision(self):
        lock.acquire()
        try:
            if self.getx() < -340 and self.gety() < self.paddle1.gety() + 50 and self.gety() > self.paddle1.gety() - 50:
                self.ball.dx *= -1

            elif self.getx() > 340 and self.gety() < self.paddle2.gety() + 50 and self.gety() > self.paddle2.gety() - 50:
                self.ball.dx *= -1

            elif self.gety() < self.block.ycor() + 100 and self.gety() > self.block.ycor() - 100 and self.getx() == self.block.xcor():
                self.ball.dx *= -1
        finally:
            lock.release()

    def gety(self):
        return self.y

    def getx(self):
        return self.x
