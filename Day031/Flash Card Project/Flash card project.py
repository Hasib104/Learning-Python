
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    data_dict = original_data.to_dict(orient= "records")
else:
    data_dict = data.to_dict(orient= "records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= current_card["French"], fill= "black")
    canvas.itemconfig(card_background, image= front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill= "white")
    canvas.itemconfig(card_background, image= back_img)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("words_to_learn.csv", index=False)

    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx= 50, pady=50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width= 1152, height= 648)
front_img = PhotoImage(file= "Front.png")
back_img = PhotoImage(file= "Back.png")
card_background = canvas.create_image(576, 324, image= front_img)
card_title = canvas.create_text(576, 200, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(576, 324, text="", font=("Ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row= 0, column= 0, columnspan= 2)

wrong_img = PhotoImage(file= "wrong.png")
wrong_button = Button(image= wrong_img, command= next_card)
wrong_button.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
wrong_button.grid(column= 0, row= 1)

right_img = PhotoImage(file= "right_button.png")
right_button = Button(image= right_img, command= is_known)
right_button.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
right_button.grid(column= 1, row= 1)

next_card() #show French and french word at the start

window.mainloop()