from turtle import Screen
from snake_design import SnakeBody, Food
import movements as m
import time
from game_engine import brain

game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(800,600)
game_screen.title("Snake")
game_screen.tracer(0)
game_screen.listen()


#TODO: Create a snake body (Done)

snake = SnakeBody()
game_screen.update()
snakebody = snake.body

#TODO: Move the Snake (Done)

game_status = True
commands = [m.move_forward]
counter = -2
while game_status:
    coordinate = snakebody[0].pos()
    for command in commands:
        command(snakebody[0])
    m.snakebody_movements(snakebody[1:], coordinate)
    commands = [m.move_forward]

#TODO: Control the Snake

    #decides the next command to add to commands
    key_pressed = False
    def on_key_pressed(key_name):
        global key_pressed
        if not key_pressed:
            key_pressed = True
            brain(snakebody[0], key_name)
            game_screen.ontimer(reset_key_flag, 200)


    def reset_key_flag():
        global key_pressed
        key_pressed = False


    def move_up():
        on_key_pressed("w")

    def move_down():
        on_key_pressed("s")

    def move_left():
        on_key_pressed("a")

    def move_right():
        on_key_pressed("d")

    # executes the commands depending on the keys press
    game_screen.onkey(move_up, "w")
    game_screen.onkey(move_up, "Up")
    game_screen.onkey(move_down, "s")
    game_screen.onkey(move_down, "Down")
    game_screen.onkey(move_left, "a")
    game_screen.onkey(move_left, "Left")
    game_screen.onkey(move_right, "d")
    game_screen.onkey(move_right, "Right")

    head_pos = snakebody[0].pos()
    max_xy = (game_screen.window_width()/2 - 10, game_screen.window_height() / 2 - 10)
    min_xy = (-1 * max_xy[0], -1 * max_xy[1])
#TODO: Detect collision with the food
    if counter == 0:
        food.relocate()
        counter = 90
    elif counter == -2:
        food = Food(game_screen, max_xy, min_xy)
        counter = 90
        print(counter, food.max_xy, food.min_xy)
    else:
        food.visiblity(counter)
        counter -= 1

#TODO: Create a scoreboard
#TODO: Detect collision with the wall
#TODO: Detect collision with the tail
#TODO: Update Screen
    game_screen.update()
    time.sleep(.1)
game_screen.exitonclick()
