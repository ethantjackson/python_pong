from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.pos_x = 0
        self.pos_y = 0
        self.vel_x = 2
        self.vel_y = 2

    def move(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.goto(self.pos_x, self.pos_y)


