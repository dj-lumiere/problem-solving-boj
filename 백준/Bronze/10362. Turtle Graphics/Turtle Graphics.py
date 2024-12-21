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
    for hh in range(1, t + 1):
        x, y = int(input()), int(input())
        commands = input()
        direction = 0
        visited = {(x, y): 1}
        duplicate = 0
        for cmd in commands:
            if cmd == 'F':
                dx, dy = DELTA[direction]
                x += dx
                y += dy
                if (x, y) in visited:
                    if visited[(x, y)] == 1:
                        duplicate += 1
                    visited[(x, y)] += 1
                else:
                    visited[(x, y)] = 1
            elif cmd == 'R':
                direction = (direction + 1) % 4
            elif cmd == 'L':
                direction = (direction - 1) % 4
        answer = f"Case #{hh}: {x} {y} {duplicate}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")