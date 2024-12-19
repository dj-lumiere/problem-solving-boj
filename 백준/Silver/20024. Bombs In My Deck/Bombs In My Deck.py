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
        A, B, C = (int(input()) for _ in range(3))
        max_bombs = (C - 1) // 5
        max_bombs = min(max_bombs, B)
        prob = Fraction(0, 1)
        prob_b = Fraction(1, 1)
        for b in range(0, max_bombs + 1):
            if b > 0:
                prob_b *= Fraction(B - b + 1, A - b + 1)
            else:
                prob_b = Fraction(1, 1)
            prob_non_bomb = Fraction(A - B, A - b)
            prob += prob_b * prob_non_bomb
        answer = prob.numerator / prob.denominator
        answers.append(f"{answer}")
    print(*answers, sep="\n")