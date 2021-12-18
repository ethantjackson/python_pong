from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(self.x_pos, self.y_pos)

    def up(self):
        if self.y_pos < 250:
            self.y_pos += 20
            self.goto(self.x_pos, self.y_pos)

    def down(self):
        if self.y_pos > -240:
            self.y_pos -= 20
            self.goto(self.x_pos, self.y_pos)

