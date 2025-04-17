from turtle import Screen, Turtle

BUFFER = 20
class Designer(Turtle):
    def __init__(self, length, height, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.length = length/2 - 40
        self.height = height/2 - 40
        self.color("white")
        self.pensize(5)
        self.pu()
        self.goto(-self.length, -self.height)
        self.pd()
        self.goto(-self.length, self.height)
        self.goto(self.length, self.height)
        self.goto(self.length, -self.height)
        self.goto(-self.length, -self.height)
        self.pu()
        self.goto(self.length, self.height)
