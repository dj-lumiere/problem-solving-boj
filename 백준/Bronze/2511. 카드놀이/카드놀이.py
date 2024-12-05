from fractions import Fraction
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
    for hh in range(t):
        A_cards = [int(input()) for _ in range(10)]
        B_cards = [int(input()) for _ in range(10)]
        A_points = 0
        B_points = 0
        last_winner = None
        for a, b in zip(A_cards, B_cards):
            if a > b:
                A_points += 3
                last_winner = 'A'
            elif b > a:
                B_points += 3
                last_winner = 'B'
            else:
                A_points += 1
                B_points += 1
        if A_points > B_points:
            winner = 'A'
        elif B_points > A_points:
            winner = 'B'
        else:
            if last_winner:
                winner = last_winner
            else:
                winner = 'D'
        answers.append(f"{A_points} {B_points}")
        answers.append(f"{winner}")
    print(*answers, sep="\n")