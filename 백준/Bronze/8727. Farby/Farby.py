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
        c, z, n = (int(input()) for _ in range(3))
        p = [int(input()) for _ in range(6)]
        red_needed = Fraction(p[3], 2) + p[4] + Fraction(p[5], 2)
        yellow_needed = p[0] + Fraction(p[1], 2) + Fraction(p[5], 2)
        blue_needed = Fraction(p[1], 2) + p[2] + Fraction(p[3], 2)
        red_deficit = Fraction(0) if red_needed <= c else red_needed - c
        yellow_deficit = Fraction(0) if yellow_needed <= z else yellow_needed - z
        blue_deficit = Fraction(0) if blue_needed <= n else blue_needed - n
        answer_parts = []
        for deficit in [red_deficit, yellow_deficit, blue_deficit]:
            if deficit.denominator == 1:
                answer_parts.append(str(deficit.numerator))
            else:
                rounded = precise_round(deficit.numerator, deficit.denominator, 1)
                answer_parts.append(rounded)
        answer = " ".join(answer_parts)
        answers.append(f"{answer}")
    print(*answers, sep="\n")