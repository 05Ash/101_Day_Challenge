import pandas as pd
import os
from random import randint

class Game_Data:
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.levels_path = {
            "HSK 1" : os.path.join(self.path, "assets/data/cli-hsk-1-vocabulary.csv"),
            "HSK 2" : os.path.join(self.path, "assets/data/cli-hsk-2-vocabulary.csv"),
            "HSK 3" : os.path.join(self.path, "assets/data/cli-hsk-3-vocabulary.csv")
        }
        self.correctly_guessed_word = []
        self.score = 0
        self.question_remaining = 0

    def load_data(self, key):
        path = self.levels_path[key]
        self.data = pd.read_csv(path).to_dict(orient="records")
        self.count = len(self.data)
        self.question_remaining = self.count
        self.score = 0


    def random_question(self):
        self.current = randint(0, self.question_remaining)
        self.question = self.data[self.current]
        self.chinese = self.question["Chinese"]
        self.pinyin = self.question["Pinyin"]
        self.english = self.question["English"]
        self.parts_of_speech = self.question["Part of Speech"]
