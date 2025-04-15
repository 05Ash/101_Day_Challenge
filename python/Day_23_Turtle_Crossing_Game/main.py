#declaration
from turtle import Screen
from collections import namedtuple
from player import Player
from cars import Car
from time import sleep
from gamescreen import highway_painter, Level_Writer

Coordinate = namedtuple("Coordinate", ["x", "y"])
FIELD = Coordinate(300, 300)
#Create Gamescreen
gamescreen = Screen()
gamescreen.setup(2*FIELD.x, 2*FIELD.y)
gamescreen.bgcolor("black")
gamescreen.tracer(0)
gamescreen.listen()

painter = highway_painter(FIELD)
level_writer = Level_Writer()

#Create Turtle
user = Player(FIELD.y)
#Create Cars
no_of_cars =30
cars = [Car(FIELD) for _ in range(no_of_cars)]
#Randomize Cars
game_status = True
cars_moved = []
i=0
counter = 0

while i < no_of_cars:
    if counter == 0:
        cars[i].movement()
        cars_moved.append(cars[i])
        i += 1
    for car in cars_moved:
        car.movement()
    # for car in cars:
    #     car.movement()

    counter = (counter+1)%5
#Listening keys for the Turtle to move up
#If turtle reaches the top, increase the speed
#Level calculator
#If turtle is hit by the car, game over
level = 0
while game_status:
    potential_collision = []
    player_lane = user.ycor()
    for car in cars_moved:
        car.movement(level)
        if (player_lane == car.ycor()
            or player_lane + 40 == car.ycor()
            or player_lane - 40 == car.ycor()):
            if user.distance(car) < 40:
                game_status = False
    sleep(0.1)
    gamescreen.onkey(user.move_up, "Up")
    gamescreen.onkey(user.move_down, "Down")
    gamescreen.update()
    if user.reached_finish_line():
        level += 1
        user.reset()
    level_writer.writer(level+1)

level_writer.over()
gamescreen.exitonclick()
