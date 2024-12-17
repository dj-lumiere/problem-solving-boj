# 3041번
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
        grid = [input() for _ in range(4)]
        pos = {}
        for i in range(4):
            for j in range(4):
                c = grid[i][j]
                if c != '.':
                    pos[c] = (i, j)
        target = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (1, 0), 'F': (1, 1), 'G': (1, 2), 'H': (
        1, 3), 'I' : (2, 0), 'J': (2, 1), 'K': (2, 2), 'L': (2, 3), 'M': (3, 0), 'N': (3, 1), 'O': (3, 2)}
        total = sum(abs(pos[c][0] - target[c][0]) + abs(pos[c][1] - target[c][1]) for c in target)
        answer = total
        answers.append(f"{answer}")
    print(*answers, sep="\n")