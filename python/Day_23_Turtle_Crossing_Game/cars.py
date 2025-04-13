from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, limit, shape = "square", visible = True):
        super().__init__(shape, visible)
        self.shapesize(1,3)
        self.color(self.random_color())
        self.x_limit = limit[0]
        self.y_limit = limit[1]-40
        self.pu()
        self.intialize()



    def random_color(self):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)

    def intialize(self):
        y = randint(-self.y_limit, self.y_limit)
        self.goto(self.x_limit, y)

    def movement(self):
        x = self.xcor()
        if x > -self.x_limit:
            x -= 10
            self.setx(x)

        else:
            self.ht()
