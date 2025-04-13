from turtle import Turtle

class Player(Turtle):
    def __init__(self, y_limit, shape = "turtle", visible = True):
        super().__init__(shape, visible)
        self.y_limit = y_limit
        self.pu()
        self.color("black")
        self.start = -y_limit + 30
        self.finish = y_limit - 30
        self.sety(self.start)
        self.increment = 10
        self.seth(90)


    def move_up(self):
        y = self.ycor()
        if y < self.finish:
            y += self.increment
        y = self.ycor() + self.increment
        self.sety(y)
