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
    t = INF
    answers = []
    for hh in range(t):
        N = int(input())
        if N == 0:
            break
        T = int(input())
        players = [{'id': i, 'count': 0} for i in range(N)]
        current = 0
        while True:
            for _ in range(T):
                players[current]['count'] += 1
                last = current
                current = (current + 1) % len(players)
            eliminated = last
            eliminated_player = players.pop(eliminated)
            if len(players) == 0:
                break
            counts = [p['count'] for p in players]
            if all(c == counts[0] for c in counts):
                break
            current = eliminated % len(players)
        p = len(players)
        c = players[0]['count']
        answer = f"{p} {c}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")