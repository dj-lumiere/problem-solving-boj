from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr
from itertools import permutations, product

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
        a, b, c = (int(input()) for _ in range(3))
        operators = ['+', '-', '*']
        max_val = -INF
        for nums in permutations([a, b, c]):
            for ops in permutations(operators, 2):
                expr_val = eval(f"{nums[0]}{ops[0]}{nums[1]}{ops[1]}{nums[2]}")
                if expr_val > max_val:
                    max_val = expr_val
        answer = max_val
        answers.append(f"{answer}")
    print(*answers, sep="\n")