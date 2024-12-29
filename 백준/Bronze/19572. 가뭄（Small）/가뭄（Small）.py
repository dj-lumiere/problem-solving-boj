from decimal import getcontext
from sys import stderr, stdout

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
        d1, d2, d3 = (int(input()) for _ in range(3))
        a_num = d1 + d2 - d3
        b_num = d1 + d3 - d2
        c_num = d2 + d3 - d1
        if a_num > 0 and b_num > 0 and c_num > 0:
            a = precise_round(a_num, 2, 1)
            b = precise_round(b_num, 2, 1)
            c = precise_round(c_num, 2, 1)
            answer = f"1\n{a} {b} {c}"
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")