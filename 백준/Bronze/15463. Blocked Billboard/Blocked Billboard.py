from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        x1, y1, x2, y2 = (int(input()) for _ in range(4))
        x3, y3, x4, y4 = (int(input()) for _ in range(4))
        xt1, yt1, xt2, yt2 = (int(input()) for _ in range(4))
        area = lambda xa, ya, xb, yb: max(0, xb - xa) * max(0, yb - ya)
        overlap = lambda xa, ya, xb, yb, xc, yc, xd, yd: max(0, min(xb, xd) - max(xa, xc)) * max(0, min(yb, yd) - max(ya, yc))
        area1 = area(x1, y1, x2, y2)
        area2 = area(x3, y3, x4, y4)
        overlap1 = overlap(x1, y1, x2, y2, xt1, yt1, xt2, yt2)
        overlap2 = overlap(x3, y3, x4, y4, xt1, yt1, xt2, yt2)
        answer = area1 + area2 - overlap1 - overlap2
        answers.append(f"{answer}")
    print(*answers, sep="\n")