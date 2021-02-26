import turtle
import pandas

screen = turtle.Screen()
screen.title("ALGERIA States")
image = "algeria_states_blank.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("48_states.csv")
states = data.state.to_list()
list_of_answers = []

while len(list_of_answers) < 50:
    user_answer = screen.textinput(title=f"{len(list_of_answers)}/48 States",
                                   prompt="What's the next state?").title()
    if user_answer == "Exit":
        missing_states = []
        for state in states:
            if state not in list_of_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv ")
        break
    if user_answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        list_of_answers.append(user_answer)

# turtle.mainloop()
# screen.exitonclick()
