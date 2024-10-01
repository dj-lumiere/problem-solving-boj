from collections import deque
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
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        a, b, c = int(input()), int(input()), int(input())
        heights = [(a, (N // a) * a), (b, (N // b) * b), (c, (N // c) * c), (a, (N // a + 1) * a),
                   (b, (N // b + 1) * b), (c, (N // c + 1) * c)]
        heights.sort(key=lambda x: (abs(x[1] - N), x[0]))
        best_block_height, best_tower_height = heights[0]
        answers.append(f"{best_block_height} {best_tower_height}")
    print(*answers, sep="\n")