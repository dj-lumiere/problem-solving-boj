from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

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
        A = [int(input()) for _ in range(n)]
        B = [int(input()) for _ in range(n)]
        prev_winner = None
        current_streak = 0
        max_streak = 0
        for i in range(n):
            a = A[i]
            b = B[i]
            if a == b:
                winner = "B" if prev_winner == "A" else "A"
            elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
                winner = "A"
            else:
                winner = "B"
            if winner == prev_winner:
                current_streak += 1
            else:
                current_streak = 1
            prev_winner = winner
            if current_streak > max_streak:
                max_streak = current_streak
        answer = max_streak
        answers.append(f"{answer}")
    print(*answers, sep="\n")