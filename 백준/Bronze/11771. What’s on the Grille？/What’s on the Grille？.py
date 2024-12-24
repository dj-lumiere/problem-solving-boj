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
        n = int(input())
        grille = [input() for _ in range(n)]
        encrypted = input()
        coverage = [[False] * n for _ in range(n)]
        valid = True
        current_grille = grille
        rotations = 4
        for _ in range(rotations):
            for i in range(n):
                for j in range(n):
                    if current_grille[i][j] == '.':
                        if coverage[i][j]:
                            valid = False
                            break
                        coverage[i][j] = True
            if not valid:
                break
            current_grille = [''.join([current_grille[n - j - 1][i] for j in range(n)]) for i in range(n)]
        if not all(all(row) for row in coverage) or not valid:
            answer = "invalid grille"
            answers.append(f"{answer}")
            continue
        grid = [[''] * n for _ in range(n)]
        current_grille = grille
        pointer = 0
        for _ in range(rotations):
            for i in range(n):
                for j in range(n):
                    if current_grille[i][j] == '.':
                        grid[i][j] = encrypted[pointer]
                        pointer += 1
            current_grille = [''.join([current_grille[n - j - 1][i] for j in range(n)]) for i in range(n)]
        decrypted = ''.join([''.join(row) for row in grid])
        answer = decrypted
        answers.append(f"{answer}")
    print(*answers, sep="\n")