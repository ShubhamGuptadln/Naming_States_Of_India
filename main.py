import turtle
import pandas
from turtle import Turtle, Screen

turtle.title("States of India")
image = 'mapIndia.gif'
Screen().addshape(image)
turtle.shape(image)

#getting the coordinate of the states

# def get_mouse_click_cor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
score = 0
data = pandas.read_csv('statesCoordinates.csv')
state = list(data["state"])
correct_answer_state = []
missing_state=[]
print(state)
for i in range(29):
    t = Turtle()
    s = Screen()
    t.penup()
    t.hideturtle()
    name = turtle.textinput(title=f'{score}/29 states correct', prompt="What's state name")
    name = name.title()
    if name=='Exit':
        break
    if name in state and name not in correct_answer_state:
        correct_answer_state.append(name)
        score += 1
        for st in state:
            if st not in correct_answer_state:
                missing_state.append(st)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("Missing states.csv")

        state_data = data[data.state == name]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(name)

turtle.write(f"Attempts ends your final score is {score}/29")
#print(missing_state)
#turtle.exitonclick()
# # turtle.mainloop()
