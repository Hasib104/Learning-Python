
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="What's another state name?")
    answer_state_title_cased = answer_state.title()

    if answer_state_title_cased == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state_title_cased in all_states:
        guessed_states.append(answer_state_title_cased)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state_title_cased] #getting the row datas
        #t.goto(state_data.x, state_data.y) #this will show error - _tkinter.TclError: bad screen distance "34    175.0
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state_title_cased)
        #t.write(state_data.state.item())

