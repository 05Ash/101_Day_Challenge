from doctest import OutputChecker
from tkinter import *
from support import mile_km_converter

title_var = ["","Miles to Kilometers","Kilometers to Miles"]
direction = 1
my_app = Tk()
my_app.title(title_var[1])
my_app.minsize(100,100)
my_app.config(padx=20, pady=20)



# app_title = Label(text = title_var[1], font=("Arial", 24, "bold"))
# app_title.grid(row=0, column=1, padx=10, pady=10)

input_labels = ["", "Miles", "Kilometers"]
input_label = Label(text = input_labels[direction], font=("Arial", 18, "bold"), width=10)
input_label.grid(row=1, column=0, padx=10, pady=10)

output_label = Label(text = input_labels[direction*-1], font=("Arial", 18, "bold"), width=10)
output_label.grid(row=1, column=2, padx=10, pady=10)


input = Entry(width=10)
input.grid(row=2, column=0)
input.insert(END, "1")
input.focus()

ans = Variable()
ans.set(mile_km_converter(1, 1))
output = Entry(width=10, textvariable=ans)
output.grid(row=2, column=2, padx=10, pady=10)

def button_clicked():
    ans.set(mile_km_converter(int(input.get()), direction))



def direction_change():
    global direction
    direction *= -1
    ans.set(mile_km_converter(int(input.get()), direction))
    my_app.title(title_var[direction])
    input_label["text"] = input_labels[direction]
    output_label["text"] = input_labels[direction*-1]



convert_button = Button(text = "Convert", command = button_clicked)
convert_button.grid(row=3, column=1, padx=10, pady=10)

direction_button = Button(text = "<==>", command = direction_change)
direction_button.grid(row=2, column=1, padx=10, pady=10)

my_app.mainloop()
