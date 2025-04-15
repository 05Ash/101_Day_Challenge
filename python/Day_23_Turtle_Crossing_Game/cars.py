from turtle import Turtle
from random import choice

CHOSEN_LANES = []

COLORS = ["red", "orange", "yellow", "blue", "green", "cyan", "magenta"]

class Car(Turtle):
    """Create cars to move inside the gamescreen"""
    def __init__(self, limit, shape = "square", visible = True):
        super().__init__(shape, visible)
        self.shapesize(1,3)
        self.random_color()
        self.x_limit = limit[0]
        self.y_limit = limit[1]-40
        self.increment = 5
        self.pu()
        self.lanes = range(-(self.y_limit-40), self.y_limit-40, 40)
        self.intialize()

    def random_color(self):
        color = choice(COLORS)
        self.color(color)

    def intialize(self):
        y = choice(self.lanes)
        while y in CHOSEN_LANES:
            y = choice(self.lanes)
        if len(CHOSEN_LANES) > 8:
            CHOSEN_LANES.pop(0)
        CHOSEN_LANES.append(y)
        self.goto(self.x_limit+50, y)


    def movement(self, level = 0):
        """Define how a car moves across the screen"""
        x = self.xcor()
        if x > -self.x_limit - 50:
            x -= self.increment + level
            self.setx(x)
        else:
            self.restart()

    def restart(self):
        self.random_color()
        self.intialize()
