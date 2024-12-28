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
        n = int(input())
        times = [input() for _ in range(n)]
        cp_start = 6 * 60 + 30
        cp_end = 19 * 60
        cp_times = []
        for time in times:
            h, m = map(int, time.split(':'))
            total = h * 60 + m
            if cp_start <= total <= cp_end:
                cp_times.append(total)
        if not cp_times:
            charge = 0
        else:
            first = min(cp_times)
            last = max(cp_times)
            if 390 <= first <= 600:
                if 390 <= last <= 960:
                    charge = 24000
                elif 961 <= last <= 1140:
                    charge = 36000
                else:
                    charge = 0
            elif 601 <= first <= 960:
                if 601 <= last <= 960:
                    charge = 16800
                elif 961 <= last <= 1140:
                    charge = 24000
                else:
                    charge = 0
            else:
                charge = 0
        answer = charge
        answers.append(f"{answer}")
    print(*answers, sep="\n")