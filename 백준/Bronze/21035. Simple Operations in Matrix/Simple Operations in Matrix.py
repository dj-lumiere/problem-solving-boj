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
        n, m = int(input()), int(input())
        matrix = [[int(input()) for _ in range(m)] for _ in range(n)]
        q = int(input())
        for _ in range(q):
            part, k, val = input(), int(input()) - 1, int(input())
            if part == 'row':
                for j in range(m):
                    matrix[k][j] += val
            elif part == 'col':
                for i in range(n):
                    matrix[i][k] += val
        s = sum(sum(row) for row in matrix)
        mn = min(min(row) for row in matrix)
        mx = max(max(row) for row in matrix)
        answer = f"{s} {mn} {mx}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")