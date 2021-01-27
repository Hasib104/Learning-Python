
from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
STEP = 0
TIMER = None

window = Tk()
window.title("Pomodoro Technique")
window.minsize(width=400, height=300)
window.config(padx= 100, pady= 50, bg=YELLOW)

title_label = Label(text="Timer", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 50, "normal"))
title_label.grid(column= 1, row= 0)

canvas = Canvas(width= 200, height= 233, bg=YELLOW, highlightthickness= 0)
img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 117, image= img)
timer_text = canvas.create_text(100, 130, text= "00.00", fill= "white", font=(FONT_NAME, 35, "bold") )
canvas.grid(column= 1, row= 1)

def start_timer():
    global STEP
    STEP += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if STEP % 2 != 0:
        timer_countdown(work)
        title_label.config(text="Work", fg=GREEN)
    elif STEP % 2 == 0:
        timer_countdown(short_break)
        title_label.config(text="Break", fg=PINK)
    elif STEP % 8 == 0:
        timer_countdown(long_break)
        title_label.config(text="Long Break", fg=RED)

def reset_timer():
    global STEP
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text= "00.00")
    title_label.config(text= "Timer")
    check_marks.config(text= "")
    STEP = 0

#Countdown Mechanism
def timer_countdown(count): #WORK_MIN * 60 = count

    count_min = math.floor(count / 60)
    count_sec = count % 60

# ***Python Dynamic Typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}") #using timer_text to show countdown using count value
    if count > 0:
        global TIMER
        TIMER = window.after(1000, timer_countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for counter in range(int(STEP/2)):
            marks += "✔"
        check_marks.config(text= marks)

start_button = Button(text= "Start", highlightthickness= 0, command= start_timer)
start_button.grid(column= 0, row=2)

reset_button = Button(text= "Reset", highlightthickness= 0, command= reset_timer)
reset_button.grid(column=2 ,row= 2)

check_marks = Label(fg= GREEN, bg= YELLOW)
check_marks.grid(column=1 ,row= 3)

window.mainloop()