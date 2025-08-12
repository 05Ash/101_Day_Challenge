# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
from time import sleep
import os
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔️"
timer_fn = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global check_count
    check_count = 0
    reset_button.config(state="disabled")
    start_button.config(state="normal")
    heading_label.config(text = "Timer", fg = GREEN)
    check_write(check_count)
    canvas.itemconfig(canvas_time, text = "00:00")
    app_window.after_cancel(timer_fn)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    time = WORK_MIN * 60
    start_button.config(state= "disabled")
    reset_button.config(state="normal")
    heading_label.config(text= "Work", fg = GREEN)
    countdown(time)

def break_countdown():
    global check_count
    if check_count <= 3:
        break_time = SHORT_BREAK_MIN * 60
        heading_label.config(text= "Break", fg = PINK)
    else:
        break_time = LONG_BREAK_MIN * 60
        heading_label.config(text= "Break", fg = RED)
        app_window.after(break_time, reset)
    countdown(break_time, True)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(counter_sec, break_time = False):
    global check_count, timer_fn
    if counter_sec >= 0:
        minutes = counter_sec // 60
        seconds = counter_sec % 60
        text_update = f"{minutes:02d}:{seconds:02d}"
        canvas.itemconfig(canvas_time, text = text_update)
        if counter_sec == 0 and not break_time:
            check_count += 1
            check_write(check_count)
            break_countdown()
        if break_time and counter_sec == 0:
            start_button.config(state="normal")
        timer_fn = app_window.after(1000, countdown, counter_sec-1, break_time)

def check_write(count):
    check_label.config(text = CHECK_MARK*count)
# ---------------------------- UI SETUP ------------------------------- #
app_window = Tk()
app_window.title("Pomodoro")
app_window.config(padx=100, pady =100, bg =YELLOW)


# Setting text variable
text_variable = StringVar()
text_variable.set("00:00")

# Heading
heading_label = Label(app_window, text = "Timer", font = (FONT_NAME, 50, "bold"), bg = YELLOW, fg = GREEN)
heading_label.grid(row=1, column = 2)

scrip_dir = os.path.dirname(__file__)
print(scrip_dir)
image_path = os.path.join(scrip_dir, "tomato.png")
print(image_path)
canvas = Canvas(app_window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
# canvas.image = tomato_img
canvas.create_image(100, 112, image = tomato_img)

canvas_time = canvas.create_text(100, 140, text = text_variable.get(), fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=2, column =2)

start_button = Button(app_window, text="START", font = (FONT_NAME, 14, "bold" ), bg="white", command=start_countdown)
start_button.config(padx=-10, pady=-10)
start_button.grid(row=3, column=1)

reset_button = Button(app_window, text="RESET", font = (FONT_NAME, 14, "bold" ), bg="white", command=reset, state= "disabled")
reset_button.config(padx=-10, pady=-10)
reset_button.grid(row=3, column=3)

check_count = 0
check_label = Label(app_window, text = "", fg=GREEN, bg = YELLOW, font = (FONT_NAME, 30, "bold" ))
check_label.grid(row=4, column=2)
app_window.mainloop()
