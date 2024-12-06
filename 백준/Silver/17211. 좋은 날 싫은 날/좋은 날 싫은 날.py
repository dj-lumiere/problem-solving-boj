from decimal import Decimal
from math import sqrt
from sys import stderr, stdout


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
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        initial_mood = int(input())
        p1 = Decimal(input())
        p2 = Decimal(input())
        p3 = Decimal(input())
        p4 = Decimal(input())
        dp = [[Decimal('0') for _ in range(2)] for _ in range(N + 1)]
        dp[0][initial_mood] = Decimal('1')
        for day in range(N):
            for mood in range(2):
                if dp[day][mood] == Decimal('0'):
                    continue
                if mood == 0:
                    dp[day + 1][0] += dp[day][0] * p1
                    dp[day + 1][1] += dp[day][0] * p2
                else:
                    dp[day + 1][0] += dp[day][1] * p3
                    dp[day + 1][1] += dp[day][1] * p4
        p_good = dp[N][0]
        p_bad = dp[N][1]
        p_good_scaled = round(p_good * 1000)
        p_bad_scaled = round(p_bad * 1000)
        answer = f"{p_good_scaled}\n{p_bad_scaled}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")