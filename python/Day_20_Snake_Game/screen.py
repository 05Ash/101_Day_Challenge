from turtle import Turtle, Screen

BUFFER = 20

class GameScreen:
    """Define screens, its range of coordinates, makes a gamefield"""
    def __init__(self, snake):
        self.screen = Screen()
        self.setupScreen()
        self.pen = Turtle()
        self.score_pen = Turtle()
        self.setupPen(self.pen)
        self.setupPen(self.score_pen)
        self.key_pressed = False
        self.snake = snake
        self.max_x = (self.screen.window_width()/2 - BUFFER)
        self.min_x = -1 * self.max_x
        self.max_y = (self.screen.window_height()/2 - BUFFER)
        self.min_y = -1 * self.max_y
        self.game_field()

    def onkey(self, funct, key):
        self.screen.onkey(funct, key)

    def ontimer(self, funct, time):
        self.screen.ontimer(funct, time)

    def setupScreen(self):
        self.screen.setup(800, 600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.screen.listen()

    def setupPen(self, pen):
        pen.ht()
        pen.width(4)
        pen.color("white")

    def exit_on_click(self):
        self.screen.exitonclick()

    def screen_update(self):
        self.screen.update()

    def game_field(self):
        self.pen.pu()
        self.pen.goto(self.min_x, self.min_y)
        self.pen.pd()
        self.pen.goto(self.min_x, self.max_y)
        self.pen.goto(self.max_x, self.max_y)
        self.pen.goto(self.max_x, self.min_y)
        self.pen.goto(self.min_x, self.min_y)
        self.pen.pu()

    def write_score(self, score, status):
        self.score_pen.goto((self.min_x+50, self.max_y-40))
        self.score_pen.pd()
        self.score_pen.clear()
        self.score_pen.write(f"Score: {score}", align = "center", font = ("Arial", 15, "bold"))
        if not status:
            self.score_pen.pu()
            self.score_pen.goto((0,0))
            self.score_pen.write("GAME OVER", align = "center", font = ("Arial", 15, "bold"))
        self.score_pen.pu()
