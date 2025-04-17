import os
import pandas as pd
from PIL import Image
from turtle import Screen
from scoreboard import Pen, Scoreboard

scrip_dir = os.path.dirname(__file__)
image_path = os.path.join(scrip_dir, "./assets/blank_states_img.gif")
file_path = os.path.join(scrip_dir, "./assets/50_states.csv")

img = Image.open(image_path)
WIDTH, HEIGHT = img.size

data = pd.read_csv(file_path)

gamescreen = Screen()
gamescreen.setup(WIDTH, HEIGHT)
gamescreen.bgcolor("black")
gamescreen.title("USA States Game")
gamescreen.bgpic(image_path)
gamescreen.tracer(0)

pen = Pen()
score = Scoreboard()
game_status = True

while game_status:
    to_check = gamescreen.textinput("State", "Your Answer: ").strip().title()
    to_write = data[data["state"] == to_check]
    score.update_score()
    if not to_write.empty:
        score.increase_score()
        score.update_score()
        pen.data_write(to_write)
    else:
        game_status = False
        score.update_high_score()
        score.write_high_score()

    gamescreen.update()


gamescreen.exitonclick()
