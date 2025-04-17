from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.width = 3
        self.pu()
        self.high_score = 0
        self.color("white")
        self.goto(0, 270)
        self.load_highscore()
        self.update_score()

    def update_score(self):
        self.pd()
        self.clear()
        self.write(f"Score: {self.score}",
                   move = False, align = "Center",
                   font = ("Arial", 15, "bold"))
        self.pu()

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write(f"GAME OVER\nHIGH SCORE: {self.high_score}", move = False, align = "center", font = ("Arial", 15, "bold"))
        self.pu()

    def update_highscore(self):
        self.high_score = max(self.score, self.high_score)
        with open("./Day_20_Snake_Game/high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def load_highscore(self):
        with open("./Day_20_Snake_Game/high_score.txt", "r") as file:
            self.high_score = int(file.read())
    # def high_score_update(self):
    #     with open("high_score.txt", "w") as file:
