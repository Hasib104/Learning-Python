
"""#Password Manager with json without catching exception"""
# from tkinter import *
# from tkinter import messagebox #module
# import random
# import pyperclip
# import json
#
# def password_generator():
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
#     password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
#     password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]
#
#     password_list = password_letters + password_symbols + password_numbers
#     random.shuffle(password_list)
#     password = "".join(password_list)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
#
# def save():
#     website = website_entry.get()
#     email = email_username_entry.get()
#     password = password_entry.get()
#     new_data = {
#         website: {
#             "email" : email,
#             "password" : password,
#         }
#     }
#
#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Error", message="Please dont leave any field empty.")
#     else:
#             with open("data.json", "r") as data_file:
#                 #reading old data
#                 data = json.load(data_file)
#                 #updating old data with new data
#                 data.update(new_data)
#
#             with open("data.json", "w") as data_file:
#                 #saving updated data
#                 json.dump(data, data_file, indent=4)  # indent=4 makes the data more suitable for usage
#                 website_entry.delete(0, END)
#                 #email_username_entry.delete(0, END)
#                 password_entry.delete(0, END)
#
# window = Tk()
# window.title("Password Manager")
# window.config(padx= 20, pady= 20)
#
# canvas = Canvas(width= 200, height= 200, highlightthickness= 0)
# logo = PhotoImage(file= "logo.png")
# canvas.create_image(100, 100, image= logo)
# canvas.grid(column= 1, row= 0)
#
# website_label = Label()
# website_label.config(text= "Website:")
# website_label.grid(column= 0, row= 1)
#
# website_entry = Entry(width= 35)
# website_entry.focus()
# website_entry.grid(column= 1, row= 1, columnspan= 2)
#
# email_username_label = Label()
# email_username_label.config(text= "Email/Username:")
# email_username_label.grid(column= 0, row= 2)
#
# email_username_entry = Entry(width= 35)
# email_username_entry.insert(0, "hasibkamalaraf@gmail.com")
# #email_username_entry.insert(END, "asd")
# email_username_entry.grid(column= 1, row= 2, columnspan= 2)
#
# password_label = Label()
# password_label.config(text= "Password")
# password_label.grid(column= 0, row= 3)
#
# password_entry = Entry(width= 21)
# password_entry.grid(column= 1, row= 3)
#
# generate_button = Button(text= "Generate Password", command= password_generator)
# generate_button.grid(column= 2, row= 3)
#
# add_button = Button(text= "Add", width= 36, command= save)
# add_button.grid(column= 1, row= 4, columnspan= 2)
#
# window.mainloop()


"""#Password Manager with json with catching exception"""

from tkinter import *
from tkinter import messagebox #module
import random
import pyperclip
import json

def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    #new_data is a structure for json
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please dont leave any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else: #if there is a previous data then we update the old data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # indent=4 makes the data more suitable for usage

        finally:    #this isn't necessary
            website_entry.delete(0, END)
            #email_username_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)

canvas = Canvas(width= 200, height= 200, highlightthickness= 0)
logo = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= logo)
canvas.grid(column= 1, row= 0)

website_label = Label()
website_label.config(text= "Website:")
website_label.grid(column= 0, row= 1)

website_entry = Entry(width= 35)
website_entry.focus()
website_entry.grid(column= 1, row= 1, columnspan= 2)

email_username_label = Label()
email_username_label.config(text= "Email/Username:")
email_username_label.grid(column= 0, row= 2)

email_username_entry = Entry(width= 35)
email_username_entry.insert(0, "hasibkamalaraf@gmail.com")
#email_username_entry.insert(END, "asd")
email_username_entry.grid(column= 1, row= 2, columnspan= 2)

password_label = Label()
password_label.config(text= "Password")
password_label.grid(column= 0, row= 3)

password_entry = Entry(width= 21)
password_entry.grid(column= 1, row= 3)

generate_button = Button(text= "Generate Password", command= password_generator)
generate_button.grid(column= 2, row= 3)

add_button = Button(text= "Add", width= 36, command= save)
add_button.grid(column= 1, row= 4, columnspan= 2)

search_button = Button(text="Search", width=15, command= find_password)
search_button.grid(column= 2, row= 1)

window.mainloop()