from math import sqrt
from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


def is_prime(v):
    if v < 2:
        return False
    if v == 2:
        return True
    if v % 2 == 0:
        return False
    for i in range(3, int(sqrt(v)) + 1, 2):
        if v % i == 0:
            return False
    return True


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        v = int(input())
        answers.append(f"Input value: {v}")
        if is_prime(v):
            answers.append("Would you believe it; it is a prime!")
        else:
            lower = v - 1
            while lower >= 2 and not is_prime(lower):
                lower -= 1
            upper = v + 1
            while not is_prime(upper):
                upper += 1
            if lower < 2:
                d = upper - v
            else:
                d_lower = v - lower
                d_upper = upper - v
                d = min(d_lower, d_upper)
            answers.append(f"Missed it by that much ({d})!")
        answers.append("")
    print(*answers, sep="\n")