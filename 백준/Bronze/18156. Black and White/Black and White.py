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
    answers = []
    t = 1
    for _ in range(t):
        n = int(input())
        grid = [input() for _ in range(n)]
        correct = 1
        half = n // 2
        for row in grid:
            if row.count('B') != half or row.count('W') != half or 'BBB' in row or 'WWW' in row:
                correct = 0
                break
        if correct:
            for col in zip(*grid):
                s = ''.join(col)
                if s.count('B') != half or s.count('W') != half or 'BBB' in s or 'WWW' in s:
                    correct = 0
                    break
        answer = correct
        answers.append(str(answer))
    print(*answers, sep="\n")