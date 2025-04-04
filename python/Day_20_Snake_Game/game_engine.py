
def statusCheck(head_pos, body, screen):
    i = 0
    for seg in body[3:]:
        if (
            seg.pos()[0] - 8 < head_pos[0] < seg.pos()[0] + 8
            and seg.pos()[1] - 8 < head_pos[1] < seg.pos()[1] + 8
            ):
            return False

    if (
        head_pos[0] >= screen.max_x - 10
        or head_pos[0] <= screen.min_x + 10
        or head_pos[1] <= screen.min_y + 10
        or head_pos[1] >= screen.max_y - 10
    ):
        return False
    return True
