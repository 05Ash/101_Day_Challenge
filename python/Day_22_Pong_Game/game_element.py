from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self, x_limit, y_limit, shape = "circle", visible = True):
        super().__init__(shape, visible)
        self.color("white")
        self.x_limit = x_limit
        self.y_limit = y_limit - 10
        self.draw_line()
        self.increment = 10
        self.pu()

    def get_heading(self):
        self.home()
        heading = randint(-30, 30)
        return heading

    def draw_line(self):
        counter = 1
        self.width(5)
        for y in range(-320, 320, 30):
            self.pu()
            if counter < 0:
                self.pd()
            self.goto(0,y)
            counter *= -1
    def ball_movement(self):
        if self.y_limit < self.ycor() or self.ycor() < -self.y_limit:
            new_heading = -self.heading()
            self.seth(new_heading)
        if -self.x_limit < self.xcor() < self.x_limit:
            self.fd(10)
            return True
        return False

    def is_struck(self, pos):

        x, y = pos
        if (x - 20 < self.xcor() < x-10) and (y - 50 < self.ycor() < y + 50):
            new_heading = 180 - self.heading()
            self.seth(new_heading)
            return True
        return False



class Score(Turtle):
    def __init__(self, coordinate, shape = "square", visible=False):
        super().__init__(shape, visible)
        self.score = 0
        self.pu()
        self.width(10)
        self.ht()
        self.color("white")
        self.goto(coordinate)

    def update_score(self):
        self.clear()
        self.write(self.score, False, "center", ("Courier", 80, "bold") )

    def increase_score(self):
        self.score += 1

    def game_end(self, score_1, score_2):
        self.home()
        if score_1 > score_2:
            to_write = "Player 1 Wins"
        else: to_write = "Player 2 Wins"
        self.write(to_write, False, "center", ("Arial", 24, "bold"))
