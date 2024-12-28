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
        n, m = int(input()), int(input())
        S = [0] * (n + 1)
        A = [0] * (n + 1)
        for __ in range(m):
            a, b, p, q = int(input()), int(input()), int(input()), int(input())
            S[a] += p
            A[a] += q
            S[b] += q
            A[b] += p
        max_W = -INF
        min_W = INF
        for i in range(1, n + 1):
            if S[i] == 0 and A[i] == 0:
                W = 0
            else:
                W = (S[i] * S[i] * 1000) // (S[i] * S[i] + A[i] * A[i])
            if W > max_W:
                max_W = W
            if W < min_W:
                min_W = W
        answers.append(str(max_W))
        answers.append(str(min_W))
    print(*answers, sep="\n")