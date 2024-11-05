from itertools import permutations, combinations
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        D = [int(input()) for _ in range(N)]
        prefix_not1 = [0] * (N + 1)
        for i in range(N):
            prefix_not1[i + 1] = prefix_not1[i] + (0 if D[i] == 1 else 1)
        suffix_not2 = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            suffix_not2[i] = suffix_not2[i + 1] + (0 if D[i] == 2 else 1)
        min_changes = INF
        for i in range(N + 1):
            changes = prefix_not1[i] + suffix_not2[i]
            if changes < min_changes:
                min_changes = changes
        answer = min_changes
        answers.append(f"{answer}")
    print(*answers, sep="\n")