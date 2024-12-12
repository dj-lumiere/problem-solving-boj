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
        M, N = int(input()), int(input())
        grid = [[False] * N for _ in range(M)]
        x, y = 0, 0
        grid[x][y] = True
        dir_idx = 0
        turns = 0
        total = M * N
        visited = 1
        while visited < total:
            dx, dy = DELTA[dir_idx]
            nx, ny = x + dx, y + dy
            if is_inbound(nx, M, ny, N) and not grid[nx][ny]:
                x, y = nx, ny
                grid[x][y] = True
                visited += 1
            else:
                dir_idx = (dir_idx + 1) % 4
                turns += 1
        answer = turns
        answers.append(f"{answer}")
    print(*answers, sep="\n")