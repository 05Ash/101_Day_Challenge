from tkinter import *
import os
from tkinter import messagebox
from wonderwords import RandomWord
import secrets
import pyperclip

FONT = ("Calibri", 15, "normal")

# Paths
dir_path = os.path.dirname(__file__)
logo_path = os.path.join(dir_path, "logo.png")
password_path = os.path.join(dir_path, "passwords.csv")

# Window
app = Tk()
app.config(padx=50, pady=50, bg="white")
app.title("Password Manager")

# Password Generator
def generate_password():
    rw = RandomWord()
    noun = rw.word(include_parts_of_speech=["nouns"]).capitalize()
    verb = rw.word(include_parts_of_speech=["verbs"]).capitalize()
    adj = rw.word(include_parts_of_speech=["adjectives"]).capitalize()
    number = secrets.randbelow(100)
    symbol = secrets.choice("!@#$%&*_")
    password = f"{adj}{noun}{verb}{symbol}{number}"
    if len(password) > 32:
        generate_password()
    pass_var.set(password)
    pyperclip.copy(password)

# Add Password
def add_password():
    website = web_var.get()
    email = mail_var.get()
    password = pass_var.get()
    if not website or not password:
        messagebox.showwarning(title="Invalid Input", message="Either Email or Password is empty.\nPlease enter valid input.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered.\nEmail: {email}\nPassword: {password}\nDo you want to save?")
        if is_ok:
            with open(password_path, "a") as file:
                file.write(f"{website}, {email}, {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)



#canvas
logo=PhotoImage(file=logo_path)
canvas = Canvas(app, width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

# Variables
web_var = StringVar()
mail_var = StringVar()
pass_var = StringVar()

# Labels and fields
website_label = Label(bg="white", text="Website:", font=FONT, pady=2)
website_label.grid(column=0, row=1)
website_entry = Entry(bg="white", width=50, textvariable=web_var)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_label = Label(bg="white", text="Email/Username:", font=FONT, pady=2)
email_label.grid(column=0, row=2)
email_entry = Entry(bg="white", width=50, textvariable=mail_var)
email_entry.insert(0, "wuxiatranslators@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_label = Label(bg="white", text="Password:",font=FONT, pady=2)
password_label.grid(column=0, row=3)
password_entry = Entry(bg="white", width=33, textvariable=pass_var)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=14, bg="white", pady=2, command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(bg="white", text="Add", width=48, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)
app.mainloop()
