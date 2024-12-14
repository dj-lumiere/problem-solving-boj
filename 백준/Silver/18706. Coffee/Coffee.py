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
    t = int(input())
    answers = []
    for _ in range(t):
        C, P = int(input()), int(input())
        coffee = {}
        for _ in range(C):
            N, S, M, L = input(), int(input()), int(input()), int(input())
            coffee[N] = {'small': S, 'medium': M, 'large': L}
        orders = []
        for _ in range(P):
            X, Y, Z = input(), input(), input()
            orders.append((X, Y, Z))
        delivery_fee = 100 // P
        for order in orders:
            name, size, cname = order
            cost = coffee[cname][size] + delivery_fee
            mod = cost % 5
            if mod == 1:
                cost -= 1
            elif mod == 4:
                cost += 1
            answer = f"{name} {cost}"
            answers.append(f"{answer}")
    print(*answers, sep="\n")