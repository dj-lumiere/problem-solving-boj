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
        N, K = int(input()), int(input())
        stalls = [0] * (N + 2)
        stalls[0] = stalls[-1] = 1
        last_y, last_z = 0, 0
        for _ in range(K):
            max_min = -1
            max_max = -1
            chosen = -1
            for i in range(1, N + 1):
                if stalls[i] == 0:
                    left = 0
                    j = i - 1
                    while j >= 0 and stalls[j] == 0:
                        left += 1
                        j -= 1
                    right = 0
                    j = i + 1
                    while j < N + 2 and stalls[j] == 0:
                        right += 1
                        j += 1
                    current_min = min(left, right)
                    current_max = max(left, right)
                    if current_min > max_min or (current_min == max_min and current_max > max_max):
                        max_min = current_min
                        max_max = current_max
                        chosen = i
            stalls[chosen] = 1
            last_y, last_z = max_max, max_min
        answer = f"Case #{hh + 1}: {last_y} {last_z}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")