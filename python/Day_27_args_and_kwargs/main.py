from tkinter import *

FONT=("Times New Roman", 16, "normal")
prog_window = Tk()

prog_window.minsize(500, 300)
prog_window.title("Kilometer to Mile Convertor")
prog_window.config(bg="white", padx = 40, pady=40)


def km_to_mile(num):
    return round(num * 0.621371, 5)

def mile_to_km(num):
    return round(num * 1.60934, 5)

def unit_converter():
    global mile_entry, km_entry

    if float(mile.get()) != mile_entry:
        input = mile_entry = float(mile.get())
        output = km_entry = mile_to_km(input)
        km_variable.set(str(output))

    elif float(km.get()) != km_entry:
        input = km_entry = float(km.get())
        output = mile_entry = km_to_mile(input)
        mile_variable.set(str(output))

km_entry = None
mile_entry = None
heading = Label(prog_window, text="Length", background="white", font=("Times New Roman", 20, "bold"))
heading.config(pady = 20)
heading.grid(row=1, column=4)


km_variable = StringVar()
km = Entry(prog_window, background="aliceblue", width=8, textvariable=km_variable, font = FONT)
km_variable.set("1")
km.grid(row=3, column=2)
km_entry = float(km_variable.get())

km_unit = Label(prog_window, text="Kilometer", background="white", font=FONT, width=8)
km_unit.config(pady=20, padx=20)
km_unit.grid(row=4,column=2)

equal_label = Label(prog_window, text = "=",background="white", font = ("Times New Roman", 24, "bold"), width = 2)
equal_label.grid(row=3,column=4)

mile_variable = StringVar()
mile = Entry(prog_window, background="aliceblue", width=8, textvariable=mile_variable, font =FONT)
mile_variable.set("0.621371")
mile.grid(row=3,column=5)
mile_entry = float(mile_variable.get())


mile_unit = Label(prog_window, text="Mile", background="white",font=FONT, width=8)
mile_unit.config(pady=20, padx=20)
mile_unit.grid(row=4, column=5)


enter_button = Button(prog_window, text="Convert", background="white", activebackground="gray", command=unit_converter)
enter_button.grid(row=6, column = 4)


prog_window.mainloop()
