from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_forword():
    tim.forward(10)

def move_backword():
    tim.backward(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(move_forword,"w")
screen.onkey(move_backword,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear_screen,"c")
screen.exitonclick()