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
        n, T = int(input()), int(input())
        x, y = 0, 0
        direction = 0
        prev = 0
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        for _ in range(n):
            Ti = int(input())
            Si = input()
            delta = Ti - prev
            x += delta * dx[direction]
            y += delta * dy[direction]
            if Si == "left":
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            prev = Ti
        delta = T - prev
        x += delta * dx[direction]
        y += delta * dy[direction]
        answer = f"{x} {y}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")