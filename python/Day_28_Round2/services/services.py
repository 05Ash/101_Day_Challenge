import tkinter as tk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Pomodoro Timer")
        self.config(padx=50, pady=50, bg = "yellow")
