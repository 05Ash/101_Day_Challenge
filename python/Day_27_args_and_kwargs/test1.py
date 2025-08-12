import tkinter

app_window = tkinter.Tk()
app_window.title("My First Gui Program")
app_window.minsize(width=640, height=480)

my_label = tkinter.Label(text= "App", font = ("Arial", 24, "bold", "italic"))
my_label.pack(expand=True)
app_window.mainloop()
