from turtle import Turtle
from random import randint

# addshape


class SnakeBody:
    def __init__(self):
        self.body = []
        self.snake()
        self.writing_head = None
        self.create_pen()

    def create_segment(self, cor):
        "Adds a segment to the snake, with cordinate given as an argument"
        new_segment = Turtle(shape= 'square')
        new_segment.color("white")
        new_segment.pu()
        new_segment.speed(1)
        new_segment.goto(cor)
        return new_segment

    def snake(self):
        """Create the initial snake"""
        for i in range(3):
            segment = self.create_segment((-20*i, 0))
            self.body.append(segment)

    def add_segment(self):

        position = self.body[-1].pos()
        new_segment = self.create_segment(position)
        self.body.append(new_segment)

    def create_pen(self):
        self.writing_head = Turtle(shape='circle')
        self.writing_head.pu()
        self.writing_head.color("white")
        self.writing_head.ht()



class Food:
    def __init__(self, screen, max_xy, min_xy, snakebody):
        self.coordinate = None
        self.screen = screen
        self.food = None
        self.max_xy = max_xy
        self.min_xy = min_xy
        self.snakebody = snakebody
        self.shape()

    def shape(self):
        self.screen.addshape("diamond", ((10,0), (0,-10),(-10,0),(0,10)))
        self.food = Turtle(shape = "diamond")
        self.food.color("white")
        self.food.pu()
        self.relocate(self.snakebody)

    def relocate(self, body):
        self.coordinate = (randint(self.min_xy[0], self.max_xy[0]), randint(self.min_xy[1], self.max_xy[1]))
        for seg in body:
            seg_x = seg.xcor()
            seg_y = seg.ycor()
            if (
                seg_x -10 < self.coordinate[0] < seg_x+10
                and seg_y -10 < self.coordinate[1] < seg_y -10
            ):
                self.relocate(body)
        self.food.goto(self.coordinate)

    def visiblity(self, counter):
        """Show or hide turtle depending on counter"""
        if not counter % 5:
            self.food.ht()
        else:
            self.food.st()
