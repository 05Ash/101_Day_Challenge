from turtle import Turtle
import os

script_dir = os.path.dirname(__file__)
high_score_path = os.path.join(script_dir, "./assets/high_score.txt")

FONT = ("Arial", 10, "bold")

class Pen(Turtle):

    def __init__(self, shape = "circle", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.pencolor("black")
        self.shapesize(0.5)
        self.pensize(4)
        self.pu()

    def data_write(self, location):
        self.goto(int(location.x), int(location.y))
        self.write(location.iloc[0]["state"], False, "center", FONT)

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.pencolor("black")
        self.pensize(6)
        self.pu()
        self.score = 0
        with open(high_score_path, "r") as file:
            self.high_score = int(file.read())

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.goto(0, 225)
        self.clear()
        self.write(f"SCORE: {self.score}", False, "center", FONT)

    def update_high_score(self):
        print(type(self.high_score), self.high_score)
        if self.score > self.high_score:
            self.high_score = self.score
            with open(high_score_path, "w") as file:
                file.write(str(self.high_score))

    def write_high_score(self):
        self.home()
        self.write(f"Your Score: {self.score}\nHigh Score: {self.high_score}\nGAME OVER", False, "center", FONT)
