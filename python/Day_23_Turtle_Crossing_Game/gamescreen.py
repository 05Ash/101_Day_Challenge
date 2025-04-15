from turtle import Turtle
def highway_painter (field):
    """Create a turtle to paint the gamescreen"""
    x_limit = field[0]+40
    y_limit = field[1]-80
    lanes = range(-y_limit-20, y_limit, 20)
    painter = Turtle()
    painter.color("white")
    painter.width(2)
    painter.ht()
    counter = 0
    painter.pu()
    print(-y_limit)
    painter.goto(0, -y_limit - 70)
    painter.write("START", True, "Center", ("Arial", 18, "bold"))
    painter.goto(0, y_limit + 50)
    painter.write("FINISH", True, "Center", ("Arial", 18, "bold"))
    for lane in lanes:
        x = x_limit + 40
        painter.pu()
        painter.goto(x, lane)
        painter.pd()
        if counter:
            i = 0
            while x > -x_limit-40:
                if not i:
                    painter.pu()
                else:
                    painter.pd()
                painter.bk(40)
                i = (i + 1)%2
                x -= 40

        painter.goto(-x, lane)
        counter = (counter + 1)%2

class Level_Writer(Turtle):
    """Creates a turtle to write to the screen"""
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.pu()
        self.goto(-220, 250)

    def writer(self, level):
        """write the level of the game on the screen, need the value of level"""
        self.clear()
        self.write(f"LEVEL {level}", False, "center", ("Arial", 20, "normal"))

    def over(self):
        """Write to the screen if the game is over"""
        self.home()
        self.write(f"GAME OVER", True, "center", ("Arial", 20, "bold"))
