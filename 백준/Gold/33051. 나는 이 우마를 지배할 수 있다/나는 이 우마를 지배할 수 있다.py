from itertools import combinations_with_replacement
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
    t = 1
    answers = []
    for hh in range(t):
        n, k, m = (int(input()) for _ in range(3))
        k -= 1
        m -= 1
        games = [[int(input()) for _ in range(8)] for _ in range(n)]
        score_sums = [0, 0, 0, 0]
        rank_sums = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for game in games:
            for i in range(4):
                rank_sums[game[i] - 1][i] += 1
            for i in range(4, 8):
                score_sums[game[i - 4] - 1] += game[i]
        answer = -1
        for d4, d3, d2 in combinations_with_replacement(range(-100, 101), 3):
            d1 = 0 - d4 - d3 - d2
            if d1 > 100:
                continue
            if d2 > d1:
                continue
            uma_score = [d1, d2, d3, d4]
            ranking_score = [0, 0, 0, 0]
            for i in range(4):
                ranking_score[i] += score_sums[i]
                for j in range(4):
                    ranking_score[i] += rank_sums[i][j] * uma_score[j]
            for i in range(4):
                ranking_score[i] *= 10
                ranking_score[i] += 3 - i
            if sorted(ranking_score, reverse=True)[m] == ranking_score[k]:
                answer = f"{d1} {d2} {d3} {d4}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")