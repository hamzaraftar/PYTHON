import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color  = (r,g,b)
    return random_color


directions = [0,90,180,270]
tim.pensize(14)
for _ in range(200):
    tim.color(randomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))

