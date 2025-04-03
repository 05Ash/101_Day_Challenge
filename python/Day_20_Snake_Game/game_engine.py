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

def statusCheck(head, body, max_xy, min_xy):
    head_cor = head.pos()
    for seg in body:
        if (
            seg.pos()[0] - 2 <= head_cor[0] < seg.pos()[0] + 2
            and seg.pos()[1] - 2 <= head_cor[1] < seg.pos()[1] + 2
            ) :
            return False

    if (
        head_cor[0] >= max_xy[0]
        or head_cor[0] <= min_xy[0]
        or head_cor[1] <= min_xy[1]
        or head_cor[1] >= max_xy[1]
    ):
        return False
    return True

def write_score(head, score, max_y, game_status):
    head.goto((0, max_y-30))
    head.pd()
    head.clear()
    head.write(f"Score: {score}", align = "center", font = ("Arial", 15, "bold"))
    if not game_status:
        head.pu()
        head.goto((0,0))
        head.write("GAME OVER", align = "center", font = ("Arial", 15, "bold"))
    head.pu()
