from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, shape = "square", visible = True):
        super().__init__(shape, visible)
        self.shapesize(3,1)
        self.color(self.random_color())

    def random_color(self):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)
