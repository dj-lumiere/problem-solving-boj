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
        dp_A_splitter = [(0, 0)] * (n + 1)
        dp_B_splitter = [(0, 0)] * (n + 1)
        for m in range(1, n + 1):
            x = m // 2
            y = m - x
            B_eat = max(x, y)
            remaining = min(x, y)
            A_eat_next, B_eat_next = dp_B_splitter[remaining]
            dp_A_splitter[m] = (A_eat_next, B_eat_next + B_eat)
            A_eat_current = max(x, y)
            remaining_B = min(x, y)
            A_eat_next2, B_eat_next2 = dp_A_splitter[remaining_B]
            dp_B_splitter[m] = (A_eat_next2 + A_eat_current, B_eat_next2)
        A_total, B_total = dp_A_splitter[n]
        answer = f"{A_total} {B_total}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")