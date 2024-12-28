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
        N, M = int(input()), int(input())
        distances_down = [int(input()) for _ in range(N - 1)]
        distances_right = [int(input()) for _ in range(M)]
        distances_down.append(distances_right[0])
        answer = ""
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                valid = True
                for i in range(1, N):
                    if abs(i - r) + abs(1 - c) != distances_down[i - 1]:
                        valid = False
                        break
                if not valid:
                    continue
                for j in range(1, M + 1):
                    if abs(N - r) + abs(j - c) != distances_right[j - 1]:
                        valid = False
                        break
                if valid:
                    answer = f"{r} {c}"
                    break
            if answer:
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")