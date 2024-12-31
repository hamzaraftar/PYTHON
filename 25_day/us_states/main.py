import turtle 
import pandas
screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

aswer_state = turtle.textinput(title="Guess the state" , prompt="What's another state's  name")
print(aswer_state)








