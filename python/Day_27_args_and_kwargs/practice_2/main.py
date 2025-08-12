import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width = 640, height = 480)

#Label
my_label = tkinter.Label(text = "I'm a Label", font= ("Arial", 24, "bold"))
my_label.pack(side= "top")

window.mainloop()
