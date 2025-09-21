from controller import gui_controller as gui

from services.tools import miles_to_km as func

from tkinter import StringVar

def convertor():
    mile = input_box.get()
    output_var.set(func(mile))


root = gui.App()

heading = gui.Label(master=root, text="Mile To Kilometer", col=2, row=1)

input_label = gui.Label(master=root, text = "MILE", row=2, col=1)

output_label = gui.Label(master=root, text = "KILOMETER", row = 2, col = 3)

input_var = StringVar(value="1")

output_var = StringVar(value = "1.61")

input_box = gui.Input(master=root, textvariable=input_var, row = 3, col = 1)

output_box = gui.Input(master=root, textvariable=output_var, row = 3, col = 3)

convert_button = gui.Button(text = "Convert", row = 4, col = 2, width=15, command=convertor)

root.mainloop()
