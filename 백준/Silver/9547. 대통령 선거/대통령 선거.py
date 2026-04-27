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
    for _ in range(t):
        C, V = int(input()), int(input())
        preferences = []
        for _ in range(V):
            pref = list(map(int, [input() for _ in range(C)]))
            preferences.append(pref)
        vote_count = [0] * (C + 1)
        for pref in preferences:
            vote_count[pref[0]] += 1
        majority = V // 2 + 1
        winner = -1
        round_num = 1
        for i in range(1, C + 1):
            if vote_count[i] >= majority:
                winner = i
                break
        if winner == -1:
            candidates = sorted([(vote_count[i], i) for i in range(1, C + 1)], key=lambda x: (-x[0], x[1]))
            top1, top2 = candidates[0][1], candidates[1][1]
            vote_round2 = [0] * (C + 1)
            for pref in preferences:
                for cand in pref:
                    if cand == top1 or cand == top2:
                        vote_round2[cand] += 1
                        break
            if vote_round2[top1] > vote_round2[top2]:
                winner = top1
            else:
                winner = top2
            round_num = 2
        answer = f"{winner} {round_num}"
        answers.append(answer)
    print(*answers, sep="\n")