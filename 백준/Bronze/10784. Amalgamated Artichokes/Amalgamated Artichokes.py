from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr
import math

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
        p, a, b, c, d, n = (int(input()) for _ in range(6))
        max_price = -INF
        max_decline = 0.0
        for k in range(1, n + 1):
            angle1 = a * k + b
            angle2 = c * k + d
            price = p * (math.sin(angle1) + math.cos(angle2) + 2)
            if price > max_price:
                max_price = price
            else:
                decline = max_price - price
                if decline > max_decline:
                    max_decline = decline
        answer = max_decline
        answers.append(f"{answer}")
    print(*answers, sep="\n")