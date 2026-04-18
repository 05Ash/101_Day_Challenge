
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
count = 0
rest = False
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, count
    count = 0
    if timer:
        app.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_marks.config(text="✔"*count)
    title_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global timer, count
    count += 1
    check_marks.config(text="✔"*(count//2))
    if count % 8 == 0:
        title_label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)
    elif count % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(t:int):
    global count, rest
    canvas.itemconfig(timer_text, text=f"{t//60:02}:{t%60:02}")
    if t > 0:
        global timer
        timer = app.after(1000, countdown, t-240)
    elif t == 0 and count == 8:
        reset_timer()

    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
import os
from tkinter import *

BASE_DIR = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(BASE_DIR, "tomato.png")

app = Tk()

app.title("Pomodoro")
app.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=2, row=0)
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=2, row=1)

start_button = Button(width=6, height=1, text="Start", font=(FONT_NAME, 14, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)
stop_button = Button(width=6, height=1, text="Stop", font=(FONT_NAME, 14, "bold"), highlightthickness=0, command = reset_timer)
stop_button.grid(column=3, row=3)
check_marks = Label(text="✔"*count, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=2, row=4)
app.mainloop()
