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
        pineapple = 0
        blueberry = 0
        last_spray = {}
        for _ in range(n):
            ti, ai, bi = int(input()), int(input()), int(input())
            team = 'pineapple' if 1 <= ai <= 4 else 'blueberry'
            if team == 'pineapple':
                pineapple += 100
                if ai in last_spray and ti - last_spray[ai] <= 10:
                    pineapple += 50
            else:
                blueberry += 100
                if ai in last_spray and ti - last_spray[ai] <= 10:
                    blueberry += 50
            last_spray[ai] = ti
        answer = f"{pineapple} {blueberry}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")