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
        B, E = int(input()), int(input())
        bessie_moves = []
        for _ in range(B):
            distance, direction = input(), input()
            bessie_moves.append((int(distance), direction))
        elsie_moves = []
        for _ in range(E):
            distance, direction = input(), input()
            elsie_moves.append((int(distance), direction))
        bessie_pos = 0
        elsie_pos = 0
        bessie_idx = 0
        elsie_idx = 0
        bessie_steps = 0
        elsie_steps = 0
        moos = 0
        last_same = True
        max_time = INF
        while bessie_idx < B or elsie_idx < E:
            if bessie_idx < B and bessie_steps == 0:
                bessie_move = bessie_moves[bessie_idx]
                bessie_dir = -1 if bessie_move[1] == 'L' else 1
                bessie_steps = bessie_move[0]
            if elsie_idx < E and elsie_steps == 0:
                elsie_move = elsie_moves[elsie_idx]
                elsie_dir = -1 if elsie_move[1] == 'L' else 1
                elsie_steps = elsie_move[0]
            if bessie_idx < B:
                bessie_pos += bessie_dir
                bessie_steps -= 1
                if bessie_steps == 0:
                    bessie_idx += 1
            if elsie_idx < E:
                elsie_pos += elsie_dir
                elsie_steps -= 1
                if elsie_steps == 0:
                    elsie_idx += 1
            if bessie_pos == elsie_pos:
                if not last_same:
                    moos += 1
                last_same = True
            else:
                last_same = False
        answer = moos
        answers.append(f"{answer}")
    print(*answers, sep="\n")