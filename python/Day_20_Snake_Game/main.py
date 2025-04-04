from snake import Snake
from food import Food
from screen import GameScreen
import time
from game_engine import statusCheck

#TODO: Create a snake body (Done)

snake = Snake()
screen = GameScreen(snake)
snakebody = snake.body
pen = screen.pen
max_x = screen.max_x
max_y = screen.max_y
min_x = screen.min_x
min_y = screen.min_y
food = Food(screen, snakebody)

#TODO: Move the Snake (Done)

game_status = True
counter = 90
score = 0
while game_status:
    head = snake.head
    body = snakebody[1:]
    coordinate = head.pos()
    snake.body_movement()
    snake.head_movement()
#TODO: Control the Snake
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
        global key_pressed
        if not key_pressed:
            key_pressed = True
            controller(key_name)
            screen.ontimer(reset_key_flag, 200)
    def controller(key):
        if key == "w":
            snake.move_up()
        elif key == "s":
            snake.move_down()
        elif key == "a":
            snake.move_left()
        else:
            snake.move_right()

    screen.onkey(down, "s")
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "a")
    screen.onkey(left, "Left")
    screen.onkey(up, "w")
    screen.onkey(right, "d")
    screen.onkey(right, "Right")


# #TODO: Detect collision with the food

    head_pos = head.pos()

    if counter == 0:
        food.relocate(snakebody)
        counter = 90

    if food.isFoodEaten(head):
        score += 1
        snake.add_segment()
        food.relocate(snakebody)
        counter = 90

    else:
        food.visiblity(counter)
        counter -= 1

# #TODO: Create a scoreboard

# #TODO: Detect collision with the wall
# #TODO: Detect collision with the tail
    game_status = statusCheck(head_pos, snakebody, screen)
#     #write_score(pen, score, max_xy[1], game_status)
    screen.write_score(score, game_status)

# #TODO: Update Screen
#     game_screen.update()
    screen.screen_update()
    time.sleep(.1)

screen.exit_on_click()
