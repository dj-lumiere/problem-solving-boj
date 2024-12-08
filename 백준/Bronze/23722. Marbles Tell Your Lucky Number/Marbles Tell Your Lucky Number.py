from collections import deque
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
    for hh in range(t):
        a1, a2, a3, a4 = (int(input()) for _ in range(4))
        if a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0:
            break
        bowls = [a1, a2, a3, a4]
        while sum(1 for b in bowls if b > 0) > 1:
            min_marbles = min(b for b in bowls if b > 0)
            chosen_index = bowls.index(min_marbles)
            for i in range(len(bowls)):
                if i != chosen_index and bowls[i] > 0:
                    bowls[i] -= min_marbles
        for b in bowls:
            if b > 0:
                answer = b
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")