def sign(x):
    if not x:
        return 0
    return x // abs(x)


def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    return sign(x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3))


def has_crosspoint(
    x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int
):
    is_123_ccw = ccw(x1, y1, x2, y2, x3, y3)
    is_124_ccw = ccw(x1, y1, x2, y2, x4, y4)
    is_341_ccw = ccw(x3, y3, x4, y4, x1, y1)
    is_342_ccw = ccw(x3, y3, x4, y4, x2, y2)
    can_have_crosspoint = False
    if is_123_ccw * is_124_ccw <= 0 and is_341_ccw * is_342_ccw <= 0:
        can_have_crosspoint = True
    if (
        is_123_ccw * is_124_ccw == 0
        and is_341_ccw * is_342_ccw == 0
        and not (
            min(x1, x2) <= max(x3, x4)
            and min(x3, x4) <= max(x1, x2)
            and min(y1, y2) <= max(y3, y4)
            and min(y3, y4) <= max(y1, y2)
        )
    ):
        can_have_crosspoint = False
    return int(can_have_crosspoint)

x1, y1, x2, y2 = map(int, input().split(" "))
x3, y3, x4, y4 = map(int, input().split(" "))
print(has_crosspoint(x1, y1, x2, y2, x3, y3, x4, y4))