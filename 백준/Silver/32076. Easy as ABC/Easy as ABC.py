from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr
from itertools import product

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
        grid = [input() for _ in range(3)]
        min_word = "ZZZ"
        for i, j in product(range(3), repeat=2):
            first_letter = grid[i][j]
            for di, dj in product(range(-1, 2), repeat=2):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if not is_inbound(ni, 3, nj, 3):
                    continue
                second_letter = grid[ni][nj]
                for ddi, ddj in product(range(-1, 2), repeat=2):
                    if ddi == 0 and ddj == 0:
                        continue
                    nni, nnj = ni + ddi, nj + ddj
                    if not is_inbound(nni, 3, nnj, 3):
                        continue
                    if nni == i and nnj == j:
                        continue
                    third_letter = grid[nni][nnj]
                    word = first_letter + second_letter + third_letter
                    if word < min_word:
                        min_word = word
        answer = min_word
        answers.append(f"{answer}")
    print(*answers, sep="\n")