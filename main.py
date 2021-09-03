import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

indicator = turtle.Turtle()
indicator.hideturtle()
indicator.pu()

correct_guesses = []

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

while len(correct_guesses) < 50:
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Name a State: ").title()

    if answer == "Exit":
        missed_states = [state for state in states_list if state not in correct_guesses]
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer in states_list:
        correct_guesses.append(answer)
        x_loc = int(data[data.state == answer].x)
        y_loc = int(data[data.state == answer].y)
        indicator.goto(x_loc, y_loc)
        indicator.write(answer, align="center")

screen.exitonclick()

