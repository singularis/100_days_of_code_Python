from tkinter import *
from tkinter import messagebox
import pandas as pd
import pyperclip
from passwd_gen import gen_passwd

FONT_NAME = "Courier"
INIT_MAIL = "test@test.com"


def password_generate():
    generated_password = gen_passwd()
    password_entry.delete(0, END)
    password_entry.insert(0, string=generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data_to_file():
    incorrect_label.config(text="")
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()
    data = {"website": [website], "username": [username], "password": [password]}
    is_correct = True
    for item in data.values():
        if len(item[0]) == 0:
            incorrect_label.config(font=(FONT_NAME, 24, "italic"), text="Please fulfill all fields", fg="RED")
            is_correct = False
    if is_correct:
        is_ok = messagebox.askokcancel(title=website, message=f"There is provided data: \n "
                                                              f"Email: {username}\nPassword:{password} \nIs it okay "
                                                              f"to save ?")
        if is_ok:
            df = pd.DataFrame(data)
            df.to_csv("./data.csv", mode='a')
            user_entry.delete(0, 'end')
            user_entry.insert(END, INIT_MAIL)
            password_entry.delete(0, 'end')
            website_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=10)

canvas = Canvas(width=200, height=200, highlightthickness=0)
background_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=background_img)
canvas.grid(column=1, row=0)

website_label = Label(font=(FONT_NAME, 12, "italic"), text="Website")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.insert(END, string="test")
website_entry.grid(column=1, row=1, columnspan=2)

user_label = Label(font=(FONT_NAME, 12, "italic"), text="Email/Username")
user_label.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.insert(END, string=INIT_MAIL)
user_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(font=(FONT_NAME, 12, "italic"), text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.insert(0, string="test")
password_entry.grid(column=1, row=3)

gen_passwd_btn = Button(text="Generate", command=password_generate, width=10, padx=0)
gen_passwd_btn.grid(column=2, row=3)

add_passwd_btn = Button(text="Add", highlightthickness=0, command=add_data_to_file, width=33)
add_passwd_btn.grid(column=1, row=4, columnspan=2)

incorrect_label = Label(font=(FONT_NAME, 24, "italic"), text="", fg="RED")
incorrect_label.grid(column=0, row=5, columnspan=3)

window.mainloop()
