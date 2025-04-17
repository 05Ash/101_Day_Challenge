from turtle import Turtle
from random import randint

BUFFER = 20

class Food(Turtle):

    def __init__(self, snakebody, width, height):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.pu()
        self.st()
        self.coordinate = None
        self.food = None
        self.x_max = width/2 - 50
        self.y_max = height/2 - 50
        self.snakebody = snakebody
        self.relocate(self.snakebody)


    def relocate(self, body):
        self.coordinate = self.generate_random_coordinate()
        coordinate_clash = True
        count = 0
        while coordinate_clash:
            for seg in body:
                seg_x = seg.xcor()
                seg_y = seg.ycor()
                count += 1
                if (
                    seg_x - BUFFER < self.coordinate[0] < seg_x + BUFFER
                    and seg_y - BUFFER < self.coordinate[1] < seg_y + BUFFER
                ):
                    coordinate_clash = True
                    self.coordinate = self.generate_random_coordinate()
                    break
            if count == len(body):
                coordinate_clash = False
        self.goto(self.coordinate)

    def generate_random_coordinate(self):
        x_cor = randint(-self.x_max+5, self.x_max-5)
        y_cor = randint(-self.y_max+5, self.y_max-5)
        return (x_cor, y_cor)

    def visiblity(self, counter):
        """Show or hide turtle depending on counter"""
        if not counter % 5:
            self.ht()
        else:
            self.st()

    def isFoodEaten(self, head):
        head_xcor = head.xcor()
        head_ycor = head.ycor()
        is_eaten = (
            self.xcor() - 20 <= head_xcor <= self.xcor() + 20
            and self.ycor() - 20 <= head_ycor <= self.ycor() + 20
                    )
        return is_eaten
