import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor())

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
answers_list = []
while len(answers_list) < 50:
    state_answer = screen.textinput(title=f"{len(answers_list)}/50 States",
                                    prompt="What's another state's name?").title()
    if state_answer == "Exit":
        missing_states = []
        for state in states:
            if state not in answers_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv ")

        break
    if state_answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        answers_list.append(state_answer)

# screen.exitonclick()
# turtle.mainloop()
