# This is the main.py file for game, where the player guesses the U.S. states
# The initial commit code of this project was obtained from the course 100 days of code
# Run this file to play the game

import turtle
import pandas

# Set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle to write the states to the map
indicator = turtle.Turtle()
indicator.hideturtle()
indicator.pu()

correct_guesses = []

# Store the 50 states as a list using pandas
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

# If the user has not guessed all 50 states, the game continues
while len(correct_guesses) < 50:
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Name a State: ").title()

    # If the user types "Exit", the game ends and a list of missed states is generated as a csv file
    if answer == "Exit":
        missed_states = [state for state in states_list if state not in correct_guesses]
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # If the user guesses correctly, the state gets labeled on the map
    if answer in states_list:
        correct_guesses.append(answer)
        x_loc = int(data[data.state == answer].x)
        y_loc = int(data[data.state == answer].y)
        indicator.goto(x_loc, y_loc)
        indicator.write(answer, align="center")

screen.exitonclick()

