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
        N = int(input())
        sizes = [int(input()) for _ in range(N)]
        prefix_sum = [0] * (N + 1)
        for idx in range(1, N + 1):
            prefix_sum[idx] = prefix_sum[idx - 1] + sizes[idx - 1]
        total = prefix_sum[N]
        if total % 3 != 0:
            answer = "-1"
        else:
            S = total // 3
            i = -1
            j = -1
            for idx in range(1, N):
                if prefix_sum[idx] == S and i == -1:
                    i = idx
                elif prefix_sum[idx] == 2 * S and i != -1:
                    j = idx
                    break
            if i != -1 and j != -1 and j < N:
                answer = f"{i} {j}"
            else:
                answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")