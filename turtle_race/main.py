from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=600)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title="Race bet", prompt="Which turtle is going to win? Enter a color :")
print(user_bet)
turtles = []

position = -100
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-280, y=position)
    position += 50
    turtles.append(new_turtle)
race_is_on = True
while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 270:
            race_is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won ! the {winner} turtle is the winner!")
            else:
                print(f"You've lost ! the {winner} turtle is the winner!")

        else:
            random_speed = random.randint(0, 10)
            turtle.forward(random_speed)

screen.exitonclick()
