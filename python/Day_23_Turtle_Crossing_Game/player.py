from turtle import Turtle

class Player(Turtle):
    """Create a user turtle to move across the screen"""
    def __init__(self, y_limit, shape = "turtle", visible = True):
        super().__init__(shape, visible)
        self.y_limit = y_limit
        self.pu()
        self.color("white")
        self.start = -y_limit + 40
        self.finish = y_limit - 40
        self.sety(self.start)
        self.increment = 40
        self.seth(90)

    def move_up(self):
        """define how the player move upwards when up key is press"""
        y = self.ycor() + self.increment
        self.sety(y)

    def move_down(self):
        """define how the player move downwards when down key is press"""
        if self.start < self.ycor():
            y = self.ycor() - self.increment
            self.sety(y)

    def reached_finish_line(self):
        """check if the player has reached the finish line"""
        return self.ycor() >= self.finish

    def reset(self):
        """resets the player to the start line"""
        self.goto(0, self.start)
