from bisect import bisect_left, bisect_right
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        n, m = (int(input()) for _ in range(2))
        answer = "NO"
        for i in range(66):
            smallest_weight = n >> i
            possible_weights = {smallest_weight: (1 << i) - (n & ((1 << i) - 1)),
                                smallest_weight + 1: n & ((1 << i) - 1)}
            if m in possible_weights and possible_weights[m] != 0:
                answer = "YES"
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")
