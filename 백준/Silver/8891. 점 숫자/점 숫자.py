# 8891번 점 숫자 다국어한국어
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
    for _ in range(t):
        a, b = int(input()), int(input())
        s1 = 1
        while (s1 * (s1 - 1)) // 2 + 1 <= a:
            s1 += 1
        s1 -= 1
        sum_prev1 = (s1 * (s1 - 1)) // 2
        x1 = a - sum_prev1
        y1 = s1 + 1 - x1
        s2 = 1
        while (s2 * (s2 - 1)) // 2 + 1 <= b:
            s2 += 1
        s2 -= 1
        sum_prev2 = (s2 * (s2 - 1)) // 2
        x2 = b - sum_prev2
        y2 = s2 + 1 - x2
        sum_x = x1 + x2
        sum_y = y1 + y2
        sum_s = sum_x + sum_y - 1
        sum_num = (sum_s * (sum_s + 1)) // 2 - (sum_s - sum_x)
        answer = sum_num
        answers.append(f"{answer}")
    print(*answers, sep="\n")