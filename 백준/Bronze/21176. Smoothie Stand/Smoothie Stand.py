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
        k, r = (int(input()) for _ in range(2))
        ingredients = [int(input()) for _ in range(k)]
        max_revenue = 0
        for _ in range(r):
            recipe = [int(input()) for _ in range(k + 1)]
            usage = recipe[:k]
            price = recipe[k]
            if all(u == 0 for u in usage):
                continue
            num = INF
            for i in range(k):
                if usage[i] > 0:
                    num = min(num, ingredients[i] // usage[i])
            revenue = num * price
            if revenue > max_revenue:
                max_revenue = revenue
        answer = max_revenue
        answers.append(f"{answer}")
    print(*answers, sep="\n")