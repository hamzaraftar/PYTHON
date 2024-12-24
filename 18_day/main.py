import turtle as t
tim = t.Turtle()

def drew_shape(number_sides):
    angle = 360 /number_sides
    for _ in range(number_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3 , 11):
    drew_shape(shape_side_n)

