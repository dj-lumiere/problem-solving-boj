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
    for _ in range(t):
        N = int(input())
        numbers = [int(input()) for _ in range(N)]
        sorted_numbers = sorted(numbers)
        n_low = (N + 1) // 2
        n_high = N // 2
        low_tides = sorted_numbers[:n_low][::-1]
        high_tides = sorted_numbers[n_low:]
        interleaved = []
        for i in range(max(n_low, n_high)):
            if i < n_low:
                interleaved.append(low_tides[i])
            if i < n_high:
                interleaved.append(high_tides[i])
        answer = ' '.join(map(str, interleaved))
        answers.append(f"{answer}")
    print(*answers, sep="\n")