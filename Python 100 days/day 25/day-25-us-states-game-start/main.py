import turtle
from turtle import Screen
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

from go_to_location import State_Name

screen=turtle.Screen()
screen.title('us state game')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
state_name=State_Name()

guess_count=[]
print(len(guess_count))
while len(guess_count)!=50:
    ans_question=screen.textinput(title=f'{len(guess_count)}/50 states correct',prompt='what is your guess')

    data=pandas.read_csv('50_states.csv')
    row_is=data[data['state'].str.lower()==ans_question.lower()]

    if ans_question=='exit':
        remain_list=[x for x in data.state.to_list() if x not in guess_count]

        df=pandas.DataFrame(remain_list)
        df.to_csv('remain.csv')
        print(remain_list)
        break
    elif row_is.empty:
        print('value entered wrogn')
        pass
    else:
        name_is=row_is['state'].item()
        x_axis=row_is['x'].item()
        y_axis=row_is['y'].item()
        state_name.go_to_location(name_is,x_axis,y_axis)
        guess_count.append(name_is)

#states to learn.csv
