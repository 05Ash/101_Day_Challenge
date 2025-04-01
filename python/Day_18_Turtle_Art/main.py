import turtle as t
import random
import colorgram

my_turtle = t.Turtle()
my_screen = t.Screen
my_turtle.shape("circle")
# my_turtle.width(4)
t.colormode(255)
def random_color_picker():
    """Returns a random rgb tuple from 0, 255"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    # print(color_rgb)
    return (r, g, b)

def draw_shape(sides):
    """Draw a shape of polygon with sides given as argument"""
    angle = 360 / sides
    for _ in range(sides):
        my_turtle.fd(100)
        my_turtle.right(angle)

# for edges in range(3, 11):
#     random_color = random_color_picker()
#     my_turtle.color(random_color)
#     draw_shape(edges)
def  random_direction():
    direction = {
        "north" : 90,
        "south" : 270,
        "east" :0,
        "west" : 180,
    }
    return direction[random.choice(list(direction.keys()))]


def random_walk(steps):
    for _ in range(steps):
        my_choice_direction = random_direction()
        my_random_color = random_color_picker()
        my_turtle.color(my_random_color)
        my_turtle.seth(my_choice_direction)
        my_turtle.fd(10)


def draw_spirograph(total):
    """Draws a spirograph of no. of circles given as argument"""
    angle = 360/total
    for _ in range(total):
        my_turtle.color(random_color_picker())
        my_turtle.circle(100)
        my_turtle.left(angle)

color_list = [(237, 233, 221), (134, 90, 53), (200, 154, 115), (57, 30, 20), (59, 99, 118), (23, 44, 68), (129, 72, 85), (71, 107, 84), (69, 27, 36), (227, 238, 230), (121, 31, 41), (130, 33, 24), (174, 145, 50), (22, 51, 36), (186, 100, 85), (140, 168, 153), (79, 83, 25), (226, 202, 126), (132, 157, 166), (21, 90, 57), (181, 140, 149), (231, 172, 161), (166, 102, 114), (220, 231, 236), (8, 89, 108), (38, 60, 97), (239, 222, 226), (93, 148, 130), (90, 145, 152), (224, 171, 181), (171, 203, 189), (119, 126, 140), (164, 204, 210), (184, 190, 202)]

def draw_hirst_copy(steps):
    my_turtle.shape("square")
    for i in range(steps):
        my_turtle.goto([0, i*50])
        for j in range(steps):
            color = random.choice(color_list)
            my_turtle.color(color)
            my_turtle.pd()
            my_turtle.stamp()
            my_turtle.pu()
            my_turtle.fd(50)
    my_turtle.goto([0,0])


draw_hirst_copy(20)
t.exitonclick()
