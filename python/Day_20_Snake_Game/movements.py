def move_forward(snakehead):
    """Dictates the movement of snakehead, which is the first element of the snake
        It makes it move forward by 20 pixels"""
    snakehead.fd(20)

def turn_left(snakehead):
    """Dictates the movement of snakehead(snake[0]), makes it turn by 90 degrees to the left"""
    snakehead.left(90)


def turn_right(snakehead):
    """Dictates the movement of snakehead(snake[0]), makes it turn by 90 degrees to the right"""
    snakehead.right(90)

def snakebody_movements(snakebody, pos):
    """Dictates the movement of the snakebody, all the elements excluding the first element.
    It requires two arguments, the body of the snake and the current position of the snakehead"""
    coordinate = pos
    for seg in snakebody:
        next_coordinate = seg.pos()
        seg.goto(coordinate)
        coordinate = next_coordinate
