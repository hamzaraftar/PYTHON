from turtle import Turtle , Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',prompt="Which turtle will win the race? Enter color :")
y_position = [-70,-40,-10,20,50,80]

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230,y=y_position [i])

    screen.exitonclick()