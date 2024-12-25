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
        M = int(input())
        total_extra = 0
        for _ in range(M):
            B = int(input())
            choices = [int(input()) for _ in range(N)]
            sum_other = sum(choices[1:])
            actual_sum = choices[0] + sum_other
            if actual_sum <= B:
                actual = choices[0]
            else:
                actual = 0
            allowed = [1, 10, 100, 1000, 10000]
            best_choice = 0
            for ca in allowed:
                if ca + sum_other <= B and ca > best_choice:
                    best_choice = ca
            extra = best_choice - actual
            total_extra += extra
        answer = str(total_extra)
        answers.append(f"{answer}")
    print(*answers, sep="\n")