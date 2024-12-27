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
        R, C = (int(input()) for _ in range(2))
        F = [[int(input()) for _ in range(C)] for _ in range(R)]
        eaten = [[False] * C for _ in range(R)]
        sum_fruit = F[0][0]
        eaten[0][0] = True
        current = (0, 0)
        while current != (R - 1, C - 1):
            x, y = current
            max_fruit = -1
            next_pos = None
            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not eaten[nx][ny]:
                    if F[nx][ny] > max_fruit:
                        max_fruit = F[nx][ny]
                        next_pos = (nx, ny)
            if next_pos is None:
                break
            sum_fruit += F[next_pos[0]][next_pos[1]]
            eaten[next_pos[0]][next_pos[1]] = True
            current = next_pos
        answer = sum_fruit
        answers.append(f"{answer}")
    print(*answers, sep="\n")