
import tkinter

# def button_clicked():
#     #print("I got clicked")
#     my_label.config(text="I got clicked")

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("GUI")
window.minsize(width= 600, height=600)
window.config(padx= 20, pady= 20)

#label
my_label = tkinter.Label(text= "Label", font= ("Arial", 24, "normal"))
my_label.config(text= "New Text")
#my_label.pack(side= "left")
#my_label.pack()
# my_label.place(x= 0, y=0)
#my_label.place(x= 100, y=100)
my_label.grid(column=0, row=0)


#Button

button = tkinter.Button(text="Click me", command= button_clicked)
#button.pack(side="right")
#button.pack()
#button.place(x= 150, y= 150)
button.grid(column= 1, row= 1)

new_button = tkinter.Button(text="new me", command= button_clicked)
#button.pack(side="right")
#button.pack()
#button.place(x= 150, y= 150)
new_button.grid(column= 2, row= 0)

#Entry

input = tkinter.Entry(width= 10)
input.get()
#input.pack()
#input.place(x= 200, y= 200)
input.grid(column= 3, row= 2)


window.mainloop()