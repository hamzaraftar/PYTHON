n.onkey(r_paddle.go_down , 'Down')

screen.onkey(l_paddle.go_up , 'w')
screen.onkey(l_paddle.go_down , 's')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()