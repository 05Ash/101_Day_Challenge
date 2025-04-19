from tkinter import *
#window
window = Tk()
window.title("My First GUI Program")
window.minsize(500, 400)
#label
label = Label(text= "My Text", font = ("Times New Roman", 20, "bold"))
label.pack()

def button_clicked():
    to_write = input.get()
    label.config(text = to_write)
#button
button = Button(text= "Click Me", command=button_clicked)

button.pack()

input = Entry(width= 10)
input.pack()
#text box
text_box = Text(width = 20, height = 5)
text_box.focus()
text_box.insert(END, "Example Entry")
text_box.pack()
def get_text():
    text = text_box.get(1.0, END)
    label2.config(text = text)

button_2 = Button(text = "Extract text", command = get_text)
button_2.pack()
label2=Label(font = ("Times New Roman", 20, "bold"))
label2.pack()

#spin box
def spinbx_used():
    label3.config(text = spinbx.get())
spinbx = Spinbox(from_=-1, to=10,command=spinbx_used, width=3)
spinbx.pack()
label3 = Label(font=("Times New Roman", 20, "bold"))
label3.pack()

#scale

def scale_used(value):
    label4.config(text = value)

scale = Scale(from_=-10, to=10, command = scale_used)
scale.pack()
label4 = Label(font=("Times New Roman", 20, "bold"))
label4.pack()

#check button
def checked():
    label5.config(text = check_state.get())
check_state = IntVar()
check_button = Checkbutton(text = "Is On?", variable=check_state, command = checked)
check_button.pack()
label5 = Label(font = ("Times New Roman", 20, "bold"))
label5.pack()

#radio button
def radio_condition():
    label6.config(text=radio_value.get())
radio_value = IntVar()
radio1 = Radiobutton(text="Option 1", value = 1, variable=radio_value, command=radio_condition)
radio2 = Radiobutton(text = "Option 2", variable=radio_value, value = 2, command=radio_condition)
radio1.pack()
radio2.pack()
label6 =Label(font = ("Times New Roman", 20, "bold"))
label6.pack()

#listbox
def listbox_used(event):
    selection = listbox.get(listbox.curselection())

    label7.config(text=selection)

fruits= ["Apple", "Banana", "Cherry", "Dates"]
listbox = Listbox(height=4)
for item in fruits:
    listbox.insert(END, item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
label7 = Label(font = ("Times New Roman", 20, "bold"), text = "Select a Fruit")
label7.pack()


mainloop()
