from turtle import Turtle
from random import randint

BUFFER = 20

class Food:
    def __init__(self, screen, snakebody):
        self.coordinate = None
        self.food = None
        self.screen = screen
        self.snakebody = snakebody
        self.shape()

    def shape(self):
        self.food = Turtle(shape = "circle")
        self.food.color("blue")
        self.food.pu()
        self.relocate(self.snakebody)

    def relocate(self, body):
        self.coordinate = self.generate_random_coordinate()
        coordinate_clash = True
        while coordinate_clash:
            for seg in body:
                seg_x = seg.xcor()
                seg_y = seg.ycor()
                if (
                    seg_x - BUFFER < self.coordinate[0] < seg_x + BUFFER
                    and seg_y - BUFFER < self.coordinate[1] < seg_y + BUFFER
                ):
                    coordinate_clash = True
                    self.coordinate = self.generate_random_coordinate()
                    break
            coordinate_clash = False
        self.food.goto(self.coordinate)

    def generate_random_coordinate(self):
        x_cor = randint(self.screen.min_x + 10, self.screen.max_x - 10)
        y_cor = randint(self.screen.min_y + 10, self.screen.max_y - 10)
        return (x_cor, y_cor)

    def visiblity(self, counter):
        """Show or hide turtle depending on counter"""
        if not counter % 5:
            self.food.ht()
        else:
            self.food.st()

    def isFoodEaten(self, head):
        head_xcor = head.xcor()
        head_ycor = head.ycor()
        is_eaten = (
            self.coordinate[0] - BUFFER <= head_xcor <= self.coordinate[0] + BUFFER
            and self.coordinate[1] - BUFFER <= head_ycor <= self.coordinate[1] + BUFFER
                    )
        return is_eaten
