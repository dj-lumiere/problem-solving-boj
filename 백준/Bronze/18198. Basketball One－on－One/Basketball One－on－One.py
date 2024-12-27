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
        record = input()
        A = 0
        B = 0
        winner = None
        for i in range(0, len(record), 2):
            player = record[i]
            points = int(record[i + 1])
            if player == 'A':
                A += points
            else:
                B += points
            if A >= 10 and B >= 10:
                if abs(A - B) >= 2:
                    winner = 'A' if A > B else 'B'
                    break
            else:
                if A >= 11 and A - B >= 1:
                    winner = 'A'
                    break
                if B >= 11 and B - A >= 1:
                    winner = 'B'
                    break
        answer = winner
        answers.append(f"{answer}")
    print(*answers, sep="\n")