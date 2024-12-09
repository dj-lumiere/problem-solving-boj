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
    DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        M = int(input())
        grid = [input() for _ in range(N)]
        max_count = 0
        for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if x == 'M':
                continue
            for y in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if y == 'O' or y == x:
                    continue
                count = 0
                for i in range(N):
                    for j in range(M):
                        if grid[i][j] != x:
                            continue
                        for dx, dy in DELTA:
                            ni, nj = i + dx, j + dy
                            if not is_inbound(ni, N, nj, M):
                                continue
                            if grid[ni][nj] != y:
                                continue
                            ni2, nj2 = ni + dx, nj + dy
                            if not is_inbound(ni2, N, nj2, M):
                                continue
                            if grid[ni2][nj2] == y:
                                count += 1
                if count > max_count:
                    max_count = count
        answer = max_count
        answers.append(f"{answer}")
    print(*answers, sep="\n")