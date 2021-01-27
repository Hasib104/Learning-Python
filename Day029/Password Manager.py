
from tkinter import *
from tkinter import messagebox #module
import random
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please dont leave any field empty.")
    else:
        #messagebox.showinfo(title="Title", message="message")
        is_ok = messagebox.askokcancel(title=website, message=f"These details were entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok == True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} / {email} / {password}\n")
                website_entry.delete(0, END)
                #email_username_entry.delete(0, END)
                password_entry.delete(0, END)

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

window.mainloop()