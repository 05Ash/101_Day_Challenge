#declaration
from turtle import Screen
from collections import namedtuple
from player import Player
from cars import Car
from time import sleep

Coordinate = namedtuple("Coordinate", ["x", "y"])
FIELD = Coordinate(300, 300)

#Create Gamescreen
gamescreen = Screen()
gamescreen.setup(2*FIELD.x, 2*FIELD.y)
gamescreen.colormode(255)
gamescreen.tracer(0)
gamescreen.listen()

#Create Turtle
user = Player(FIELD.y)
print(user.pos())
#Create Cars
car = Car(FIELD)
#Randomize Cars
game_status = 600

while game_status:
    car.movement()
#Listening keys for the Turtle to move up
#If turtle reaches the top, increase the speed
#Level calculator
#If turtle is hit by the car, game over
    sleep(0.1)
    gamescreen.onkey(user.move_up, "space")

    gamescreen.update()


gamescreen.exitonclick()
