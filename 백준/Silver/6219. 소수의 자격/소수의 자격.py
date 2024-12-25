from sys import stdout, stderr
from math import isqrt


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
    for _ in range(t):
        A, B, D = (int(input()) for _ in range(3))
        sieve = [True] * (B + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, isqrt(B) + 1):
            if sieve[i]:
                sieve[i * i:B + 1:i] = [False] * len(range(i * i, B + 1, i))
        count = sum(1 for num in range(A, B + 1) if sieve[num] and str(D) in str(num))
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")