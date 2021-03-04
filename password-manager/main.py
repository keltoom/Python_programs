from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if website == '' or password == '':
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"There are the details entered :\n"
        #                                        f"Email: {email_username}\n"
        #                                        f"Password: {password}\nIs it okay to save? ")
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            reset()


def reset():
    website_input.delete(0, END)
    email_username_input.delete(0, END)
    email_username_input.insert(0, "keltoom@gmail.com")
    password_input.delete(0, END)
    website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "keltoom@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=25)
password_input.grid(column=1, row=3)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
