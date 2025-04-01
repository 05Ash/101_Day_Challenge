import turtle as t

tim = t.Turtle()
screen = t.Screen
tim.fd(50)
t.listen()
tim.shape("arrow")

t.mode("logo")

def move_left():
    tim.width(4)
    tim.right(10)

def move_right():
    tim.left(10)

def move_up():
    tim.width(4)
    tim.fd(10)

def move_down():
    tim.back(10)

def clear_screen():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

t.onkey(key = "d", fun = move_left)
t.onkey(key = "a", fun = move_right)
t.onkey(key = "w", fun = move_up)
t.onkey(key = "s", fun = move_down)
t.onkey(key = "c", fun = clear_screen)

t.exitonclick()
