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
        R, S, K = int(input()), int(input()), int(input())
        grid = [list(input()) for _ in range(R)]
        max_flies = -1
        best_pos = (0, 0)
        for i in range(R - K + 1):
            for j in range(S - K + 1):
                count = 0
                for x in range(i + 1, i + K - 1):
                    for y in range(j + 1, j + K - 1):
                        if grid[x][y] == '*':
                            count += 1
                if count > max_flies:
                    max_flies = count
                    best_pos = (i, j)
        i, j = best_pos
        grid[i][j] = '+'
        grid[i][j + K - 1] = '+'
        grid[i + K - 1][j] = '+'
        grid[i + K - 1][j + K - 1] = '+'
        for y in range(j + 1, j + K - 1):
            grid[i][y] = '-'
            grid[i + K - 1][y] = '-'
        for x in range(i + 1, i + K - 1):
            grid[x][j] = '|'
            grid[x][j + K - 1] = '|'
        answer = str(max_flies)
        answers.append(answer)
        for row in grid:
            answers.append(''.join(row))
    print(*answers, sep="\n")