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
    t = int(input())
    answers = []
    for hh in range(t):
        n, d, b, e = (int(input()) for _ in range(4))
        temp_n, temp_d = n, d
        digits = ''
        for _ in range(e + 1):
            temp_n *= 7
            digit = temp_n // temp_d % 7
            digits += str(digit)
            temp_n = temp_n % temp_d
            if temp_n == 0:
                digits += '0' * (e - len(digits) + 1)
                break
        result = digits[b:e + 1]
        answer = f"Problem set {hh + 1}: {n} / {d}, base 7 digits {b} through {e}: {result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")