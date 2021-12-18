from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.p1_score = 0
        self.p2_score = 0
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.p1_score, align="center", font=("Courier", 40, "bold"))
        self.goto(150, 200)
        self.write(self.p2_score, align="center", font=("Courier", 40, "bold"))

    def score_p1(self):
        self.p1_score += 1
        self.write_scores()

    def score_p2(self):
        self.p2_score += 1
        self.write_scores()
