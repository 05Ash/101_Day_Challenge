from turtle import Turtle

# addshape
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180
BUFFER = 20


class Snake:
    def __init__(self):
        self.body = []
        self.snake()
        self.head = self.body[0]
        self.score = 0
        self.high_score = 0

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

    def head_movement(self):
        self.head.fd(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def body_movement(self):
        initial_pos = self.head.pos()
        for seg in self.body[1:]:
            next_pos = seg.pos()
            seg.goto(initial_pos)
            initial_pos = next_pos

    def reset(self):
        for seg in self.body:
            seg.ht()
            del seg
        self.body.clear()
        self.snake()
        self.head = self.body[0]
