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
        time_part, utc_part = input(), input()
        HH, MM = map(int, time_part.split(':'))
        D_YJ = float(utc_part[3:])
        offset_YJ = int(D_YJ * 60)
        utc_minutes = HH * 60 + MM - offset_YJ
        utc_minutes %= 1440
        for _ in range(N):
            co_utc = input()
            D_co = float(co_utc[3:])
            offset_co = int(D_co * 60)
            co_time = (utc_minutes + offset_co) % 1440
            co_HH = co_time // 60
            co_MM = co_time % 60
            answer = f"{co_HH:02d}:{co_MM:02d}"
            answers.append(f"{answer}")
    print(*answers, sep="\n")