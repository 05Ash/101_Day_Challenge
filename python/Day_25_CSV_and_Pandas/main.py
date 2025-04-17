import os
import pandas as pd
from PIL import Image
from turtle import Screen
from scoreboard import Pen

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
game_status = True
guessed_states = []
state_list = data.state.to_list()
while game_status:
    to_check = gamescreen.textinput(f"{len(guessed_states)}/{len(data)} States Correct", "Your Guess: ").strip().title()
    to_write = data[data["state"] == to_check]
    if to_check == "Exit":
        break
    if not to_write.empty and to_check not in guessed_states:
        guessed_states.append(to_check)
        pen.data_write(to_write)

    gamescreen.update()

learn_filepath = os.path.join(scrip_dir,"./assets/states.learn.csv")
state_to_learn = []

for state in state_list:
    if state not in guessed_states:
        state_to_learn.append(state)

learning_data = pd.DataFrame(state_to_learn)
learning_data.to_csv(learn_filepath)
