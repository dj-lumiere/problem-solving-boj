from sys import stderr, stdout
from heapq import heappop, heappush

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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        level, language_score, reading_score, listening_score = (int(input()) for _ in range(4))
        minimal_total_score = [0, 100, 90, 95, 90, 80]
        if not (level == 1 or level == 2):
            answers.append("NO")
            continue
        if listening_score < 50:
            answers.append("NO")
            continue
        score_higher_than_minimal_count = 0
        score_lower_than_fail_count = 0
        if language_score * 3 < minimal_total_score[level]:
            score_higher_than_minimal_count += 1
        if reading_score * 3 < minimal_total_score[level]:
            score_higher_than_minimal_count += 1
        if language_score <= 21:
            score_lower_than_fail_count += 1
        if reading_score <= 21:
            score_lower_than_fail_count += 1
        if listening_score <= 21:
            score_lower_than_fail_count += 1
        if score_higher_than_minimal_count < 2 and score_lower_than_fail_count < 1:
            answers.append("NO")
            continue
        answers.append("YES")
    print(*answers, sep="\n")