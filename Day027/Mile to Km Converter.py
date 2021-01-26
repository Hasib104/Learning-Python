
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx= 120, pady= 120)
#window.config()
def calculate():
    result = float(input.get()) * 1.61
    result_label.config(text= f"{result}")

input = Entry(width= 7)
input.grid(column= 1, row= 0)

miles = Label()
miles.config(text= "Miles")
miles.grid(column= 2, row= 0)

is_equal_to = Label()
is_equal_to.config(text= "is equal to")
is_equal_to.grid(column= 0, row= 1)

result_label = Label()
result_label.config(text= "0")
result_label.grid(column= 1, row= 1)

km = Label()
km.config(text= "Km")
km.grid(column= 2, row= 1)

calc_button = Button(text= "Calculate", command= calculate)
calc_button.grid(column= 1, row= 2)

window.mainloop()