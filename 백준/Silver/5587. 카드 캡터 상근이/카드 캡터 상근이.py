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
        sang_cards = sorted([int(input()) for _ in range(n)])
        all_cards = set(range(1, 2 * n + 1))
        geun_cards = sorted(all_cards - set(sang_cards))
        sang = sang_cards.copy()
        geun = geun_cards.copy()
        last = 0
        turn = 'sang'
        while sang and geun:
            if turn == 'sang':
                idx = 0
                while idx < len(sang) and sang[idx] <= last:
                    idx += 1
                if idx < len(sang):
                    last = sang[idx]
                    del sang[idx]
                else:
                    last = 0
                turn = 'geun'
            else:
                idx = 0
                while idx < len(geun) and geun[idx] <= last:
                    idx += 1
                if idx < len(geun):
                    last = geun[idx]
                    del geun[idx]
                else:
                    last = 0
                turn = 'sang'
        answer = f"{len(geun)}\n{len(sang)}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")