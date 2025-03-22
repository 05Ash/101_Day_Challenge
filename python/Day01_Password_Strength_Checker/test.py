# import turtle
# my_screen = turtle.Screen()
# my_turtle = turtle.Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("coral")
# my_turtle.forward(100)
# my_screen.exitonclick()

import prettytable
my_table = prettytable.PrettyTable()
my_table.add_column("Name", ["Ash", "Shub", "Ved"])
my_table.add_column("Age", [1, 2, 3])
my_table.add_autoindex()
my_table.align = "r"

print(my_table)
