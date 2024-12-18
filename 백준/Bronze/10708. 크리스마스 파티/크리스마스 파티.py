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
        n, m = (int(input()) for _ in range(2))
        A = [int(input()) for _ in range(m)]
        scores = [0] * (n + 1)
        for i in range(m):
            Ai = A[i]
            Bi = [int(input()) for _ in range(n)]
            count_correct = 0
            for j in range(1, n + 1):
                if Bi[j - 1] == Ai:
                    scores[j] += 1
                    count_correct += 1
            count_wrong = n - count_correct
            scores[Ai] += count_wrong
        for j in range(1, n + 1):
            answers.append(f"{scores[j]}")
    print(*answers, sep="\n")