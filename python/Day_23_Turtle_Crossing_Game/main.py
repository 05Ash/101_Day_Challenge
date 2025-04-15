#declaration
from turtle import Screen
from collections import namedtuple
from player import Player
from cars import Car
from time import sleep
from gamescreen import highway_painter, Level_Writer

Coordinate = namedtuple("Coordinate", ["x", "y"])
FIELD = Coordinate(300, 300)
#Create Gamescreen, definte its size, paints it, stops the animation, and activates listeing of the screen
gamescreen = Screen()
gamescreen.setup(2*FIELD.x, 2*FIELD.y)
gamescreen.bgcolor("black")
gamescreen.tracer(0)
gamescreen.listen()

#Create a turtle to draw on the gamescreen, and initiate one to write the level on the screen
painter = highway_painter(FIELD)
level_writer = Level_Writer()

#Initiate a player for the game
user = Player(FIELD.y)

#Defines the number of cars present at one time on the screen and creates an array of them
no_of_cars =30
cars = [Car(FIELD) for _ in range(no_of_cars)]

#Defines the require variables for the game
game_status = True #True as long as the player has not crashed
cars_moved = [] #A variable to star which cars has moved from the array of cars
i=0 #index variable to move through list of cars
counter = 0 # counter to make sure the cars moved one after another

#A loop for the cars to move alternatively, closes after all cars have moved
while i < no_of_cars:
    if counter == 0:
        cars[i].movement()
        cars_moved.append(cars[i])
        i += 1
    for car in cars_moved:
        car.movement()

level = 1 #Variable to store the level of the game
while game_status:
    player_lane = user.ycor()
    #Loop to move the cars with every iteration and check if the user has not collided with the cars
    for car in cars_moved:
        car.movement(level)
        if (player_lane == car.ycor()
            or player_lane + 40 == car.ycor()
            or player_lane - 40 == car.ycor()):
            if user.distance(car) < 40:
                game_status = False

    #Slow down the looping sequence
    sleep(0.1)

    #Commands to act how the player moves across the screen
    gamescreen.onkey(user.move_up, "Up")
    gamescreen.onkey(user.move_down, "Down")
    gamescreen.update()

    #Check if the user has reached the finish line
    if user.reached_finish_line():
        level += 1
        user.reset()
    level_writer.writer(level)

#Writes game over once user is hit by the car
level_writer.over()
gamescreen.exitonclick()
