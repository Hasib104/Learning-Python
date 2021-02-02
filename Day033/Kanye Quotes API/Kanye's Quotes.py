
from tkinter import *
import requests

def next_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    ran_quote = response.json()
    canvas.itemconfig(quotes, text=ran_quote["quote"])

window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
###width of the text was given so that the longer quotes dont go over the canvas
quotes = canvas.create_text(150, 207, text="Kanye's Quote",width=250, font=("Arial", 20, "bold"))
canvas.grid(column=0, row=0)

kanye_head_img = PhotoImage(file="kanye.png")
kanye_head_button = Button(image=kanye_head_img, command= next_quote)
kanye_head_button.config(highlightthickness= 0)
kanye_head_button.grid(column=0, row=1)

window.mainloop()