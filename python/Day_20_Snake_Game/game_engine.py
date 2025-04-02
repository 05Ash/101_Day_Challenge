import movements as m

def brain(snakehead, key):
    heading = snakehead.heading()
    if (
        heading == 0 and key == "w"
        or heading == 90 and key == "a"
        or heading == 180 and key == "s"
        or heading == 270 and key == "d"
    ):
        m.turn_left(snakehead)

    elif (
        heading == 0 and key == "s"
        or heading == 90 and key == "d"
        or heading == 180 and key == "w"
        or heading == 270 and key == "a"
    ):
        m.turn_right(snakehead)
