from turtle import Turtle
import random
class Racer:
    def __init__(self, name, color, position, shape = "turtle", thickness = 4):
        self.name = name
        self.color = color
        self.shape = shape
        self.thickness = thickness
        self.position = position

    def initialize(self):
        self.name = Turtle()
        self.name.color(self.color)
        self.name.shape(self.shape)
        self.name.width(self.thickness)

    def take_position(self):
        self.name.pu()
        self.name.goto([-290, (-150 + self.position * 50)])


    def dist(self):
        return random.random()*10

    def run(self):
        distance = self.dist()
        self.name.fd(distance)

    def heading(self):
        return self.name.xcor()
