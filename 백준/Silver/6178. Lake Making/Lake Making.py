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
        R, C, E, N = (int(input()) for _ in range(4))
        elevation = [[int(input()) for _ in range(C)] for _ in range(R)]
        for _ in range(N):
            Rs, Cs, Ds = int(input()) - 1, int(input()) - 1, int(input())
            max_elev = max(elevation[r][c] for r in range(Rs, Rs + 3) for c in range(Cs, Cs + 3))
            target = max_elev - Ds
            for r in range(Rs, Rs + 3):
                for c in range(Cs, Cs + 3):
                    if elevation[r][c] > target:
                        elevation[r][c] = target
        total = 0
        for r in range(R):
            for c in range(C):
                if E > elevation[r][c]:
                    total += E - elevation[r][c]
        answer = total * 72 * 72
        answers.append(f"{answer}")
    print(*answers, sep="\n")