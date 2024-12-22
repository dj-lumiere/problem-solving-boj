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
        N = int(input())
        grid = [[0] * 1001 for _ in range(1001)]
        adj = [[0] * 1001 for _ in range(1001)]
        comfortable = set()
        for _ in range(N):
            x = int(input())
            y = int(input())
            grid[x][y] = 1
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if is_inbound(nx, 1001, ny, 1001):
                    adj[nx][ny] += 1
                    if grid[nx][ny]:
                        if adj[nx][ny] == 3:
                            comfortable.add((nx, ny))
                        elif adj[nx][ny] == 4:
                            comfortable.discard((nx, ny))
            cnt = 0
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if is_inbound(nx, 1001, ny, 1001) and grid[nx][ny]:
                    cnt += 1
            adj[x][y] = cnt
            if cnt == 3:
                comfortable.add((x, y))
            elif cnt == 4:
                comfortable.discard((x, y))
            answer = len(comfortable)
            answers.append(f"{answer}")
    print(*answers, sep="\n")