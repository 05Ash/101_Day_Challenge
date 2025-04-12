from turtle import Turtle

class Player(Turtle):
    def __init__(self, position, limit):
        super().__init__()
        self.pu()
        self.shapesize(5, 1)
        self.shape("square")
        self.color("white")
        self.y_limit = limit
        self.x_limit = position[0]
        self.goto(position)

    def move_up(self):
        if self.ycor() < self.y_limit - 50:
            self.goto(self.x_limit, self.ycor() + 20)


    def move_down(self):
        if self.ycor() > -self.y_limit + 50:
            self.goto(self.x_limit, self.ycor() - 20)
