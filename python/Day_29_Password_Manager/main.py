from tkinter import *
import os
FONT = ("Times New Roman", 16, "normal")

#dirpath
scr_path = os.path.dirname(__file__)
image_path = os.path.join(scr_path, "assets/logo.png")
pass_path = os.path.join(scr_path, "assets/passwords.csv")
# window
app_window = Tk()
app_window.minsize(width=400, height=400)
app_window.config(bg="white", padx=50, pady =50)
app_window.title("Password Manager")


#Password Generator
def generate_password():
    pass
#Password Save
def add_password():
    with open(pass_path, "a") as file:
        to_write = " , ".join([web_variable.get(), mail_variable.get(), password_variable.get(), "\n"])
        file.write(to_write)
    web_entry.delete(0, END)
    password_entry.delete(0, END)


# canvas
canvas = Canvas(app_window, width=200, height = 200, bg = "white", highlightthickness=0)
logo_image = PhotoImage(file = image_path)
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row = 0, column= 0)

#website_entry
web_variable = StringVar()
web_label = Label(app_window, background="white")
web_label.grid(row = 1, column=0)
web_entry_label = Label(web_label, text = "Website:", width = 20, font = FONT, bg = "white", pady= 10)
web_entry_label.pack(side = "left")
web_entry = Entry(web_label, font = FONT, width = 30, bg ="white", textvariable=web_variable)
web_entry.focus()
web_entry.pack(side="right")

#Email entry
mail_variable = StringVar()
mail_label = Label(app_window, background="white")
mail_label.grid(row = 2, column = 0)
mail_entry_label = Label(mail_label, text = "Email/Username", width = 20, font = FONT, bg = "white", pady= 10)
mail_entry_label.pack(side = "left")
mail_entry = Entry(mail_label, font = FONT, width=30, bg = "white", textvariable=mail_variable)
mail_entry.insert(0, "wuxiatranslators@gmail.com")
mail_entry.pack(side = "right")

# Password
password_variable = StringVar()
password_label = Label(app_window, background="white")
password_label.grid(row = 3, column=0)
password_entry_label = Label(password_label, text = "Password", width = 20, font =FONT, bg = "white", pady= 10)
password_entry_label.pack(side="left")
password_entry = Entry(password_label, font = FONT, width = 14, bg = "white", textvariable= password_variable)
password_entry.pack(side="left")
generate_button = Button(password_label, font = FONT, width = 14, bg = "white", text = "Generate Password", pady= -10)
generate_button.pack(side="left")

# Add
add_label = Label(app_window, background="white")
add_label.grid(row = 4, column =0)
add_button_label = Label(add_label, width=20, bg = "white", font=FONT, pady= 10)
add_button_label.grid(row = 0, column = 0)
add_button = Button(add_label, font = FONT, width=30, text = "Add", bg = "white", padx= -18, command = add_password)
add_button.grid(row = 0, column=1)


app_window.mainloop()
