# DECLARATIONS
from turtle import Screen
from player import Player
from collections import namedtuple
from game_element import Ball, Score
from time import sleep

Limits = namedtuple("Limits", ["x","y"])
FIELD = Limits(400,300)
PLAYER_1 = Limits(FIELD.x - 50,0)
PLAYER_2 = Limits(-FIELD.x + 50, 0)
#2> Drawing the midline
#5> creating logic to make the ball bounce of player
#7> Make score

#1> Setting up the screen
gamescreen = Screen()
gamescreen.bgcolor("black")
gamescreen.setup(2*FIELD.x,2*FIELD.y)
gamescreen.title("Pong")
gamescreen.tracer(0)
gamescreen.listen()


#3> Initiating the players
#4> shaping the player
player1 = Player(PLAYER_1, FIELD.y)
player2 = Player(PLAYER_2, FIELD.y)
player1_score = Score(coordinate=(PLAYER_1[0]/2, FIELD.y-100))
player2_score = Score(coordinate=(PLAYER_2[0]/2, FIELD.y-100))
scores = [player1_score, player2_score]
players = [player1, player2]
ball = Ball(FIELD.x, FIELD.y)
is_key_pressed = False
def controller(key):
    global is_key_pressed
    if not is_key_pressed:
        is_key_pressed = True
        if key == "w":
            player1.move_up()
        elif key == "s":
            player1.move_down()
        elif key == "Down":
            player2.move_down()
        else:
            player2.move_up()
    gamescreen.ontimer(key_pressed_reset,200)

def key_pressed_reset():
    global is_key_pressed
    is_key_pressed = False

def key_pressed_w():
    controller("w")
def key_pressed_s():
    controller("s")
def key_pressed_up():
    controller("Up")
def key_pressed_down():
    controller("Down")
def game_end():
    player1_score.game_end(player1_score.score, player2_score.score)
    gamescreen.ontimer(gamescreen.bye, 2000)



game_speed = 0.1
player_turn = 0
game_status = True
while game_status:
    ball_in_game = True
    heading = ball.get_heading() + player_turn*180
    ball.seth(heading)
    while ball_in_game:
#6> if ball misses, initiate the game
        if ball.is_struck(players[player_turn].pos()):
            player_turn = (player_turn + 1)%2
            game_speed *= .9

        if not ball.ball_movement():
            scores[(player_turn+1)%2].increase_score()
            ball_in_game = False

        gamescreen.onkey(player1.move_up, "w")
        gamescreen.onkey(player1.move_down, "s")
        gamescreen.onkey(player2.move_up, "Up")
        gamescreen.onkey(player2.move_down, "Down")
        gamescreen.onkey(game_end, "space")

        sleep(game_speed)
        # gamescreen.onkey(gamescreen.bye(),"Space")
        gamescreen.update()
    for score in scores:
        score.update_score()
    game_speed = 0.1

    player_turn = (player_turn + 1)%2


gamescreen.exitonclick()
