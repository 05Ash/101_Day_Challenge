from snake import Snake
from food import Food
from screen import Designer
import time
from game_engine import statusCheck
from score import ScoreBoard
from turtle import Screen
#TODO: Create a snake body (Done)

WIDTH = 800
HEIGHT = 600

gamescreen = Screen()

gamescreen.setup(WIDTH, HEIGHT)
gamescreen.bgcolor("black")
gamescreen.tracer(0)
gamescreen.listen()

#Design Gamescreen
design = Designer(WIDTH, HEIGHT)

#Importin snake

snake = Snake()
snakebody = snake.body

#Initiating Food
food = Food(snakebody, WIDTH, HEIGHT)

# pen = gamescreen.pen

# #TODO: Move the Snake (Done)

game_status = True
counter = 90

# Create a scoreboard
scoreboard = ScoreBoard()

gamescreen.update()

while game_status:
    head = snake.head
    body = snakebody[1:]
    coordinate = head.pos()
    snake.body_movement()
    snake.head_movement()
# Control the Snake
    key_pressed = False

    def up():
        on_key_pressed("w")

    def down():
        on_key_pressed("s")

    def left():
        on_key_pressed("a")

    def right():
        on_key_pressed("d")

    def reset_key_flag():
        global key_pressed
        key_pressed = False

    def on_key_pressed(key_name):
        """Make sure key cannot be pressed repeatedly"""
        global key_pressed
        if not key_pressed:
            key_pressed = True
            controller(key_name)
            gamescreen.ontimer(reset_key_flag, 100)

    def controller(key):
        if key == "w":
            snake.move_up()
        elif key == "s":
            snake.move_down()
        elif key == "a":
            snake.move_left()
        else:
            snake.move_right()

    gamescreen.onkey(down, "s")
    gamescreen.onkey(up, "Up")
    gamescreen.onkey(down, "Down")
    gamescreen.onkey(left, "a")
    gamescreen.onkey(left, "Left")
    gamescreen.onkey(up, "w")
    gamescreen.onkey(right, "d")
    gamescreen.onkey(right, "Right")
    gamescreen.onkey(gamescreen.bye, "Escape")


    # Detect collision with the food

    head_pos = head.pos()

    if counter == 0:
        food.relocate(snakebody)
        counter = 90

    if food.isFoodEaten(head):
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.add_segment()
        food.relocate(snakebody)
        counter = 90

    else:
        food.visiblity(counter)
        counter -= 1

    # Detect collision with the wall and tail
    in_game = statusCheck(head_pos, snakebody, design)
    if not in_game:
        snake.reset()
        scoreboard.reset()


    # Update Screen
    gamescreen.update()
    time.sleep(.1)


scoreboard.update_highscore()
scoreboard.game_over()
gamescreen.exitonclick()
