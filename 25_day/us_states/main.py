import turtle 
import pandas
screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    answer_state = turtle.textinput(title=f"  {len(guess_state)}/50 State Correct" , prompt="What's another state's  name").title()
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]    
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(answer_state)


screen.exitonclick()



