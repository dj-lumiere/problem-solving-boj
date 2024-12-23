# 15083번 Life Savings
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
        p1 = int(input())
        p2 = int(input())
        p3 = int(input())
        c1 = int(input())
        c2 = int(input())
        c3 = int(input())
        total = p1 + p2 + p3
        saving_one = precise_round(c1 * total, 100, 2)
        items = sorted([p1, p2, p3], reverse=True)
        if c2 < c3:
            c2, c3 = c3, c2
        saving_two = precise_round(c2 * items[0] + c3 * items[1], 100, 2)
        if float(saving_one) > float(saving_two):
            answer = f"one {saving_one}"
        else:
            answer = f"two {saving_two}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")