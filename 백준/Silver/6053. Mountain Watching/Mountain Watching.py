from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr


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
        n = int(input())
        heights = [int(input()) for _ in range(n)]
        max_width = 0
        left = [1] * n
        for i in range(1, n):
            if heights[i] >= heights[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if heights[i] >= heights[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
        for i in range(n):
            current_width = left[i] + right[i] - 1
            if current_width > max_width:
                max_width = current_width
        answer = max_width
        answers.append(f"{answer}")
    print(*answers, sep="\n")