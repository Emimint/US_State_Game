import turtle
import pandas as pd

screen = turtle.Screen()
image = 'blank_states_img.gif'
steps = 10

screen.title('Guess US State Game')
screen.bgpic(image)

my_pencil = turtle.Turtle(shape='blank')
my_pencil.penup()

The_States = pd.read_csv('50_states.csv')
all_states = The_States.state.to_list()
good_guesses = []


while len(all_states) > len(good_guesses):
    state_answer = screen.textinput(title=f'{len(good_guesses)}/50 Correct', prompt='Name the state').title()

    if state_answer == 'Exit':
        break
    if state_answer in all_states and state_answer not in good_guesses:
        df = The_States[The_States.state == state_answer]
        good_guesses.append(state_answer)
        location = (int(df.x),int(df.y))
        my_pencil.goto(location)
        my_pencil.write(f" {df.state.item()}", False, align="center", font=("Courier", 10, "normal"))
        # my_pencil.write(f" {state_answer}", False, align="center", font=("Courier", 10, "normal"))

my_pencil.goto(0,steps)
my_pencil.clear()
my_pencil.write(f"Congratulations! You have guessed {len(good_guesses)} states! Here are the states you have missed:", False, align="center", font=("Courier", 22, "normal"))

missed_states_list = list(set(all_states) - set(good_guesses))

# df_new[df_new['l_ext'].isin([31, 22, 30, 25, 64])]
Missed_States = The_States[The_States.state.isin(missed_states_list)]
Missed_States.to_csv('missing_states.csv')

# print (all_states)
# print (good_guesses)
# print (missed_states_list)
for missed_states in missed_states_list:
    my_pencil.goto(0, -steps)
    my_pencil.write(missed_states, font=("Courier", 8, "normal"))
    steps += 10

screen.exitonclick()