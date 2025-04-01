import race
import turtle as t
my_screen = t.Screen
t.setup(600, 400)
t.listen()
list_of_racers = []
names = ["a", "b", "c", "d", "e", "f"]
colors = ["red", "black", "blue", "green", "khaki", "yellow"]

def race_preparation(num_of_racer):
    """initialize the racers depending on no."""
    for i in range(num_of_racer):
        name = names[i] #input("Enter the name of racer: ")
        color = colors[i] #input("Enter the color of racer: ")
        name = race.Racer(name, color, i)
        name.initialize()
        name.take_position()
        list_of_racers.append(name)

def race_start():
    xcor = []
    while not any(cor > 300 for cor in xcor):
        xcor = []
        for racer in list_of_racers:
            racer.run()
            xcor.append(racer.heading())
    winner = 0
    for index in range(len(xcor)):
        if xcor[index] > xcor[winner]: winner = index
    return winner



race_preparation(len(names))
guess = input(f"Who do you think could be the winner between {'/'.join(colors)}: ")
winner = race_start()
if guess == colors[winner]:
    print("You win, you guessed it right!!!")
else:
    print(f"You lose, the winner is {colors[winner]}")

#t.onkey(fun = race_start, key = " ")
#t.exitonclick()
