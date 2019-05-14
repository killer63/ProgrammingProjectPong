from turtle import Turtle

class Pen:
    score_a = 0
    score_b = 0

    def __init__(self):
        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("0       0", align="center", font=("Courier", 24, "normal"))
    
    def a_win(self):
        self.score_a += 1
        self.pen.clear()
        self.pen.write("{}       {}".format(
            self.score_a, self.score_b), align="center", font=("Courier", 24, "normal"))

    def b_win(self):
        self.score_b += 1
        self.pen.clear()
        self.pen.write("{}       {}".format(
            self.score_a, self.score_b), align="center", font=("Courier", 24, "normal"))
