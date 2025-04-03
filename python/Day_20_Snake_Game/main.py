from turtle import Screen
from snake_design import SnakeBody, Food
import movements as m
import time
from game_engine import brain, statusCheck, write_score

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
pen = snake.writing_head

#TODO: Move the Snake (Done)

game_status = True
counter = -2
score = 0
while game_status:
    head = snakebody[0]
    body = snakebody[1:]
    coordinate = head.pos()
    m.move_forward(head)
    m.snakebody_movements(body, coordinate)

#TODO: Control the Snake

    #decides the next command to add to commands
    key_pressed = False
    def on_key_pressed(key_name):
        global key_pressed
        if not key_pressed:
            key_pressed = True
            brain(head, key_name)
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

#TODO: Detect collision with the food
    screen_width = game_screen.window_width()
    screen_height = game_screen.window_height()
    max_xy = (screen_width/2 - 10, screen_height / 2 - 10)
    min_xy = (-1 * max_xy[0], -1 * max_xy[1])

    if counter == -2:
        food = Food(game_screen, max_xy, min_xy, snakebody)
        counter = 90

    head_pos = head.pos()
    food_pos = food.coordinate
    food_eaten = ( food_pos[0]-10 <= head_pos[0] <= food_pos[0]+10 and food_pos[1]-10 <= head_pos[1] <= food_pos[1]+10)

    if counter == 0:
        food.relocate(snakebody)
        counter = 90

    elif food_eaten:
        score += 1
        snake.add_segment()
        food.relocate(snakebody)
        counter = 90

    else:
        food.visiblity(counter)
        counter -= 1

#TODO: Create a scoreboard
    game_screen.title(f"Score: {score}")

#TODO: Detect collision with the wall
#TODO: Detect collision with the tail
    game_status = statusCheck(head, body, max_xy, min_xy)
    write_score(pen, score, max_xy[1], game_status)

#TODO: Update Screen
    game_screen.update()
    time.sleep(.1)

game_screen.exitonclick()
