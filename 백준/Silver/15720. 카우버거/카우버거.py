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
        b, c, d = (int(input()) for _ in range(3))
        burgers = [int(input()) for _ in range(b)]
        sides = [int(input()) for _ in range(c)]
        drinks = [int(input()) for _ in range(d)]
        burgers.sort(reverse=True)
        sides.sort(reverse=True)
        drinks.sort(reverse=True)
        total_cost = sum(burgers + sides + drinks)
        discounted_cost = total_cost
        for i, j, k in zip(burgers, sides, drinks):
            discounted_cost -= (i + j + k) // 10
        answer = f"{total_cost}\n{discounted_cost}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")