from collections import Counter
from itertools import combinations
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(t):
        dots = [(int(input()), int(input())) for _ in range(4)]
        line_length = [(x2 - x1) ** 2 + (y2 - y1) ** 2 for (x1, y1), (x2, y2) in combinations(dots, 2)]
        line_length_count = Counter(line_length)
        answer = 1
        if len(line_length_count) != 2:
            answer = 0
        else:
            len1, len2 = sorted(line_length_count.keys())
            if not (line_length_count[len1] == 4 and line_length_count[len2] == 2):
                answer = 0
            if len1 * 2 != len2:
                answer = 0
        answers.append(f"{answer}")
    print(*answers, sep="\n")
