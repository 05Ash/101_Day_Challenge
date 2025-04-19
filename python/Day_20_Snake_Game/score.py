from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.width = 3
        self.pu()
        with open("./Day_20_Snake_Game/high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.pd()
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   move = False, align = "Center",
                   font = ("Arial", 15, "bold"))
        self.pu()

    def increase_score(self):
        self.score += 1

    def update_highscore(self):
        if self.high_score < self.score:
            with open("./Day_20_Snake_Game/high_score.txt", "w") as file:
                file.write(str(self.high_score))

    def reset(self):
        self.update_highscore()
        self.score = 0
        self.update_score()
    # def high_score_update(self):
    #     with open("high_score.txt", "w") as file:
