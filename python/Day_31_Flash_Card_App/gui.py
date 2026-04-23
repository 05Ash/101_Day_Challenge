from tkinter import *
import os
from tkinter.ttk import Combobox

class Game:
    def __init__(self) -> None:
        self.bg = "#B1DDC6"
        self.cn_font = "Noto Sans CJK SC"
        self.eng_font = "Times New Roman"
        self.window()
        self.path = os.path.dirname(__file__)
        self.right_img_path = os.path.join(self.path, "assets/images/right.png")
        self.wrong_img_path = os.path.join(self.path, "assets/images/wrong.png")
        self.front_card_path = os.path.join(self.path, "assets/images/card_front.png")
        self.back_card_path = os.path.join(self.path, "assets/images/card_back.png")
        self.start_img_path = os.path.join(self.path, "assets/images/play.png")
        self.stop_img_path = os.path.join(self.path, "assets/images/stop.png")
        self.levels = ("HSK 1", "HSK 2", "HSK 3")
        self.right_img = PhotoImage(file=self.right_img_path)
        self.wrong_img = PhotoImage(file=self.wrong_img_path)
        self.front_card_img = PhotoImage(file=self.front_card_path)
        self.back_card_img = PhotoImage(file=self.back_card_path)
        self.start_img = PhotoImage(file=self.start_img_path)
        self.stop_img = PhotoImage(file=self.stop_img_path)
        self.level_var = StringVar()
        self.flip_timer = ""
        self.initialize_canvas()
        self.center_text = self.canvas.create_text(400, 300, text="", font=(self.cn_font, 30, "bold"))
        self.bottom_text = self.canvas.create_text(400, 400, text="", font=(self.cn_font, 20, "italic"))
        self.initialize_button()
        self.level_selection()
        self.placement()


    def window(self):
        self.app = Tk()
        self.app.config(bg=self.bg, padx=20, pady=20)
        self.app.title("Flash Card App")

    def initialize_canvas(self):
        self.canvas = Canvas(self.app, height=600, width=800, bg=self.bg, highlightthickness=0)
        self.card = self.canvas.create_image(400, 300, image=self.front_card_img)

    def initialize_button(self):
        self.right_button = Button(self.app, image=self.right_img, highlightthickness=0, activebackground=self.bg, bg=self.bg)
        self.wrong_button = Button(self.app, image=self.wrong_img, highlightthickness=0, activebackground=self.bg, bg=self.bg)
        self.start_button = Button(self.app, image=self.start_img, highlightthickness=0, activebackground=self.bg, bg=self.bg)
        self.stop_button = Button(self.app, image=self.stop_img, highlightthickness=0, activebackground=self.bg, bg=self.bg)


    def level_selection(self):
        self.drop_down = Combobox(self.app, textvariable=self.level_var, state="readonly", values=self.levels)
        self.drop_down.current(0)

    def placement(self):
        self.drop_down.grid(column=0, row=0, columnspan=3)
        self.start_button.grid(column=0, row=1)
        self.stop_button.grid(column=2, row=1)
        self.canvas.grid(column=0, row=2, columnspan=3)
        self.right_button.grid(column=0, row=3)
        self.wrong_button.grid(column=2, row=3)

    def show_question(self, word, pronounciation):
        self.canvas.itemconfig(self.card, image=self.front_card_img)
        self.canvas.itemconfig(self.center_text, text=word)
        self.canvas.itemconfig(self.bottom_text, text=pronounciation)

    def show_answer(self, answer, parts_of_speech):
        self.canvas.itemconfig(self.card, image=self.back_card_img)
        self.canvas.itemconfig(self.center_text, text=answer)
        self.canvas.itemconfig(self.bottom_text, text=parts_of_speech)

    def run(self):
        self.app.mainloop()
