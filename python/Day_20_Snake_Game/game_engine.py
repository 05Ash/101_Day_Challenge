
def statusCheck(head_pos, body, screen):
    for seg in body[3:]:
        if (
            seg.xcor() - 8 < head_pos[0] < seg.xcor() + 8
            and seg.ycor() - 8 < head_pos[1] < seg.ycor() + 8
            ):
            return False

    if (
        head_pos[0] >= screen.length
        or head_pos[0] <= -screen.length
        or head_pos[1] >= screen.height
        or head_pos[1] <= -screen.height
    ):
        return False
    return True
