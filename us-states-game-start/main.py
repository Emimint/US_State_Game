import turtle
import pandas as pd

screen = turtle.Screen()
image = 'blank_states_img.gif'
num_corr_answer = 0

screen.title('Guess US State Game')
screen.bgpic(image)

state_answer = screen.textinput(title=f'{num_corr_answer}/50 Correct', prompt='Name the state').title()

The_States = pd.read_csv

print (state_answer)



screen.exitonclick()