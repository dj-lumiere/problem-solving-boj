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
        n, m = int(input()), int(input())
        cars = [(int(input()), int(input())) for _ in range(n)]
        for _ in range(m):
            xj, yj, tj = int(input()), int(input()), int(input())
            count = 0
            for ai, bi in cars:
                d = bi - ai
                distance = abs(d)
                cycle = 2 * distance
                t_mod = tj % cycle
                dir = 1 if d > 0 else -1
                if t_mod <= distance:
                    pos = ai + dir * t_mod
                else:
                    pos = bi - dir * (t_mod - distance)
                if xj <= pos <= yj:
                    count += 1
            answers.append(f"{count}")
    print(*answers, sep="\n")