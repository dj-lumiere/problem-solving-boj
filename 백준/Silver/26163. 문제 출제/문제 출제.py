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
        b = [int(input()) for _ in range(5)]
        max_fee = 0
        for a1 in range(15 // 1 + 1):
            for a2 in range(15 // 2 + 1):
                for a3 in range(15 // 3 + 1):
                    for a4 in range(15 // 4 + 1):
                        for a5 in range(15 // 5 + 1):
                            sum_a = a1 + a2 + a3 + a4 + a5
                            sum_i = a1 * 1 + a2 * 2 + a3 * 3 + a4 * 4 + a5 * 5
                            if (sum_a <= 3 and sum_i <= 10) or (sum_a >= 4 and sum_i <= 15):
                                total_fee = a1 * b[0] + a2 * b[1] + a3 * b[2] + a4 * b[3] + a5 * b[4]
                                if total_fee > max_fee:
                                    max_fee = total_fee
        answer = max_fee
        answers.append(f"{answer}")
    print(*answers, sep="\n")