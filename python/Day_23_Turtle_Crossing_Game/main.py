#declaration
from turtle import Screen
from collections import namedtuple
from player import Player

Coordinate = namedtuple("Coordinate", ["x", "y"])
FIELD = Coordinate(300, 300)

#Create Gamescreen
gamescreen = Screen()
gamescreen.setup(2*FIELD.x, 2*FIELD.y)
gamescreen.tracer(0)

#Create Turtle
user = Player()

#Create Cars
#Randomize Cars
#Listening keys for the Turtle to move up
#If turtle reaches the top, increase the speed
#Level calculator
#If turtle is hit by the car, game over

gamescreen.update()
gamescreen.exitonclick()
