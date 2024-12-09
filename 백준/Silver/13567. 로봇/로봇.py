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
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x <= size_x and 0 <= pos_y <= size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        M = int(input())
        n = int(input())
        x, y, direction = 0, 0, 1
        valid = True
        for _ in range(n):
            cmd = input()
            if cmd=='TURN':
                dir = input()
                if dir == '0':
                    direction = (direction + 3) % 4
                else:
                    direction = (direction + 1) % 4
            else:
                d = int(input())
                x += DELTA[direction][0] * d
                y += DELTA[direction][1] * d
                if not is_inbound(x, M, y, M):
                    valid = False
                    break
        if valid:
            answer = f"{x} {y}"
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
