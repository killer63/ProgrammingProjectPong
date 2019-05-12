
import turtle
import os
import threading
import time

wn = turtle.Screen()
wn.title("Ping-pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
class Paddle_A:
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("green")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)
    global lock

    #move of paddle
    def up():
        y = Paddle_A.paddle_a.ycor()
        y += 20
        Paddle_A.paddle_a.sety(y)

    def down():
        y = Paddle_A.paddle_a.ycor()
        y -= 20
        Paddle_A.paddle_a.sety(y)

    def move():
        lock.acquire()
        try:
            wn.listen()
            wn.onkeypress(Paddle_A.up, "w")
            wn.onkeypress(Paddle_A.down, "s")
        finally:
            lock.release()
    
# Paddle B
class Paddle_B:
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("blue")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)
    global lock

    #move of paddle
    def up():
        y = Paddle_B.paddle_b.ycor()
        y += 20
        Paddle_B.paddle_b.sety(y)

    def down():
        y = Paddle_B.paddle_b.ycor()
        y -= 20
        Paddle_B.paddle_b.sety(y)

    def move():
        lock.acquire()
        try:
            wn.listen()
            wn.onkeypress(Paddle_B.up, "Up")
            wn.onkeypress(Paddle_B.down, "Down")
        finally:
            lock.release()

# block
class Block: 
    block = turtle.Turtle()
    block.speed(0)
    block.shape("square")
    block.color("white")
    block.shapesize(stretch_wid=5,stretch_len=1)
    block.penup()
    block.goto(0, -200)
    block.dy = 1
    global lock

    def move():
        lock.acquire()
        try:
            Block.block.sety(Block.block.ycor() + Block.block.dy)
            if Block.block.ycor() > 290:
                Block.block.sety(290)
                Block.block.dy *= -1
            elif Block.block.ycor() < -290:
                Block.block.sety(-290)
                Block.block.dy *= -1
        finally:
            lock.release()

# Ball
class Ball:
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1
    global lock
     
     # borders of screen
    def borders():
        if Ball.ball.ycor() > 290:
            Ball.ball.sety(290)
            Ball.ball.dy *= -1

        elif Ball.ball.ycor() < -290:
            Ball.ball.sety(-290)
            Ball.ball.dy *= -1

        elif Ball.ball.xcor() > 350:
            Pen.score_a += 1
            Pen.a_win()
            Ball.ball.goto(0, 0)
            Ball.ball.dx *= -1

        elif Ball.ball.xcor() < -350:
            Pen.score_b += 1
            Pen.b_win()
            Ball.ball.goto(0, 0)
            Ball.ball.dx *= -1

    # move of the ball
    def move():
        Ball.ball.setx(Ball.ball.xcor() + Ball.ball.dx)
        Ball.ball.sety(Ball.ball.ycor() + Ball.ball.dy)
    
    # ball collisions
    def collision():
        lock.acquire()
        try:
            if Ball.ball.xcor() < -340 and Ball.ball.ycor() < Paddle_A.paddle_a.ycor() + 50 and Ball.ball.ycor() > Paddle_A.paddle_a.ycor() - 50:
                Ball.ball.dx *= -1

            elif Ball.ball.xcor() > 340 and Ball.ball.ycor() < Paddle_B.paddle_b.ycor() + 50 and Ball.ball.ycor() > Paddle_B.paddle_b.ycor() - 50:
                Ball.ball.dx *= -1

            elif Ball.ball.ycor() < Block.block.ycor() + 50 and Ball.ball.ycor() > Block.block.ycor() - 50 and Ball.ball.xcor() == Block.block.xcor():
                Ball.ball.dx *= -1
        finally:
            lock.release()

# Pen
class Pen:
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    score_a = 0
    score_b = 0

    def a_win():
        Pen.pen.clear()
        Pen.pen.write("Player A: {}  Player B: {}".format(Pen.score_a, Pen.score_b), align="center", font=("Courier", 24, "normal"))
    
    def b_win():
        Pen.pen.clear()
        Pen.pen.write("Player A: {}  Player B: {}".format(Pen.score_a, Pen.score_b), align="center", font=("Courier", 24, "normal"))
    
# Main game loop
def main():
    global lock
    
    while True:
        wn.update()
        lock = threading.Lock()
        p1 = threading.Thread(target=Ball.move(), args=())
        p2 = threading.Thread(target=Ball.borders(), args=())
        p3 = threading.Thread(target=Ball.collision(), args=())
        p4 = threading.Thread(target=Paddle_A.move(), args=())
        p5 = threading.Thread(target=Paddle_B.move(), args=())
        p6 = threading.Thread(target=Block.move(), args=())
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()

# Start a main game loop
main()
