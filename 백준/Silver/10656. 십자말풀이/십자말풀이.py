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
        n, m = int(input()), int(input())
        grid = [input() for _ in range(n)]
        clues = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    is_start = False
                    if (j == 0 or grid[i][j - 1] == '#') and j + 2 < m and grid[i][j + 1] == '.' and grid[i][
                        j + 2] == '.':
                        is_start = True
                    if (i == 0 or grid[i - 1][j] == '#') and i + 2 < n and grid[i + 1][j] == '.' and grid[i + 2][
                        j] == '.':
                        is_start = True
                    if is_start:
                        clues.append((i + 1, j + 1))
        answers.append(str(len(clues)))
        for clue in clues:
            answers.append(f"{clue[0]} {clue[1]}")
    print(*answers, sep="\n")