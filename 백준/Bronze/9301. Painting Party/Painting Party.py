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
    t = int(input())
    answers = []
    for case in range(1, t + 1):
        n = int(input())
        m = int(input())
        grid = [['.'] * n for _ in range(n)]
        for _ in range(m):
            parts = [input()] + [int(input()) for _ in range(4)] + [input()]
            shape, X, Y, W, H, C = parts
            X, Y, W, H = int(X) - 1, int(Y) - 1, int(W), int(H)
            for i in range(Y, Y + H):
                for j in range(X, X + W):
                    if shape == "Empty":
                        if i == Y or i == Y + H - 1 or j == X or j == X + W - 1:
                            grid[n - 1 - i][j] = C
                    else:
                        grid[n - 1 - i][j] = C
        answer = f"Case {case}:"
        answers.append(answer)
        for row in grid:
            answers.append(''.join(row))
    print(*answers, sep="\n")