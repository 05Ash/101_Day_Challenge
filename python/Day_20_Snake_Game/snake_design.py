from turtle import Turtle
from random import randint

# addshape


class SnakeBody:
    def __init__(self):
        self.body = []
        self.snake()

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
        heading = self.snake.body[-1].heading()
        position = list(self.snake.body[-1].pos())
        if heading == 0:
            position[0] -= 20
        elif heading == 90:
            position[1] -= 20
        elif heading == 180:
            position[0] += 20
        else:
            position[1] += 20
        new_segment = self.create_segment(position)
        self.body.append(new_segment)

class Food:
    def __init__(self, screen, max_xy, min_xy):
        self.coordinate = ()
        self.screen = screen
        self.food = None
        self.max_xy = max_xy
        self.min_xy = min_xy
        self.shape()
        self.coordinate = None

    def shape(self):
        self.screen.addshape("diamond", ((10,0), (0,-10),(-10,0),(0,10)))
        self.food = Turtle(shape = "diamond")
        self.food.color("white")
        self.food.pu()
        self.relocate()

    def relocate(self):
        self.coordinate = (randint(self.min_xy[0], self.max_xy[0]), randint(self.min_xy[1], self.max_xy[1]))
        self.food.goto(self.coordinate)

    def visiblity(self, counter):
        """Show or hide turtle depending on counter"""
        if not counter % 3:
            self.food.ht()
        else:
            self.food.st()
