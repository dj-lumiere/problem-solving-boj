from math import sqrt
from sys import stderr, stdout


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
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for _ in range(t):
        line = input()
        if line == "END":
            break
        directions = line.rstrip('.').split(',')
        x, y = 0.0, 0.0
        for direction in directions:
            if direction.endswith("NE"):
                steps = int(direction[:-2])
                dx, dy = sqrt(0.5), sqrt(0.5)
            elif direction.endswith("SE"):
                steps = int(direction[:-2])
                dx, dy = sqrt(0.5), -sqrt(0.5)
            elif direction.endswith("SW"):
                steps = int(direction[:-2])
                dx, dy = -sqrt(0.5), -sqrt(0.5)
            elif direction.endswith("NW"):
                steps = int(direction[:-2])
                dx, dy = -sqrt(0.5), sqrt(0.5)
            elif direction.endswith("N"):
                steps = int(direction[:-1])
                dx, dy = 0, 1
            elif direction.endswith("E"):
                steps = int(direction[:-1])
                dx, dy = 1, 0
            elif direction.endswith("S"):
                steps = int(direction[:-1])
                dx, dy = 0, -1
            elif direction.endswith("W"):
                steps = int(direction[:-1])
                dx, dy = -1, 0
            x += steps * dx
            y += steps * dy
        D = sqrt(x ** 2 + y ** 2)
        answer = f"You can go to ({x:.3f},{y:.3f}), the distance is {D:.3f} steps."
        answers.append(f"{answer}")
    print(*answers, sep="\n")