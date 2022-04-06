import turtle
import pandas

DATA = pandas.read_csv("./day-25/states-quiz/50_states.csv")
STATE_NAME = DATA.state

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "./day-25/states-quiz/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

turtle_state = turtle.Turtle()
turtle_state.penup()
turtle_state.hideturtle()

state_counter = 0
to_learn = STATE_NAME.to_list()
while state_counter < 50:
    answer_state = screen.textinput(
        title=f"{state_counter} of 50", prompt="What's another state?"
    ).title()
    if answer_state == "Exit":
        # send STATE_NAME not on map to csv
        states_to_learn = pandas.DataFrame(to_learn)
        states_to_learn.to_csv("./day-25/states-quiz/states_to_learn.csv")
        break
    for state in STATE_NAME:
        if answer_state in state:
            turtle_state.setpos(
                int(DATA[STATE_NAME == answer_state].x),
                int(DATA[STATE_NAME == answer_state].y),
            )
            turtle_state.write(answer_state)
            to_learn.remove(answer_state)
            state_counter += 1

# states_to_learn.csv


turtle.mainloop()
