from turtle import Turtle
from threading import Lock

lock = Lock()


class Block:
    global lock

    def __init__(self):
        self.block = Turtle()
        self.block.speed(0)
        self.block.shape("square")
        self.block.color("white")
        self.block.shapesize(stretch_wid=10, stretch_len=1)
        self.block.penup()
        self.block.goto(0, -200)
        self.block.dy = 0.8

    def move(self):
        lock.acquire()
        try:
            self.block.sety(self.block.ycor() + self.block.dy)
            if self.block.ycor() > 250:
                self.block.sety(250)
                self.block.dy *= -1
            elif self.block.ycor() < -250:
                self.block.sety(-250)
                self.block.dy *= -1
        finally:
            lock.release()
