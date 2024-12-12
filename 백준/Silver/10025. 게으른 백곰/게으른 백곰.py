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
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        k = int(input())
        arr = [0] * 1000001
        for _ in range(n):
            g = int(input())
            x = int(input())
            arr[x] += g
        prefix_sum = [0] * 1000002
        for i in range(1, 1000002):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        max_sum = 0
        for pos in range(-1, 1000002):
            left = pos - k if pos - k >= 0 else 0
            right = pos + k if pos + k <= 1000000 else 1000000
            s = prefix_sum[right] - (prefix_sum[left - 1] if left > 0 else 0)
            if s > max_sum:
                max_sum = s
        answer = max_sum
        answers.append(f"{answer}")
    print(*answers, sep="\n")