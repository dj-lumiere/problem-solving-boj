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
        N = int(input())
        x_low, x_high, y_low, y_high = -INF, INF, -INF, INF
        for _ in range(N):
            x_i = int(input())
            y_i = int(input())
            d_i = input()
            if d_i == 'L':
                x_high = min(x_high, x_i - 1)
            elif d_i == 'R':
                x_low = max(x_low, x_i + 1)
            elif d_i == 'U':
                y_low = max(y_low, y_i + 1)
            elif d_i == 'D':
                y_high = min(y_high, y_i - 1)
        if x_low > x_high or y_low > y_high:
            answer = "0"
        elif x_low == -INF or x_high == INF or y_low == -INF or y_high == INF:
            answer = "Infinity"
        else:
            answer = str((x_high - x_low + 1) * (y_high - y_low + 1))
        answers.append(f"{answer}")
    print(*answers, sep="\n")