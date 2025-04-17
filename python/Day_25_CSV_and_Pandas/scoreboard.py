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
        self.goto(location.x.item(), location.y.item())
        self.write(location.state.item(), False, "center", FONT)
