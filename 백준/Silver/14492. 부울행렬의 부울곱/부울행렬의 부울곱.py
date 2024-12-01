from itertools import product
from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for _ in range(t):
        n = int(input())
        a = [[int(input()) for _ in range(n)] for _ in range(n)]
        b = [[int(input()) for _ in range(n)] for _ in range(n)]
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i, j, k in product(range(n), repeat=3):
            result[i][k] |= a[i][j] & b[j][k]
        total_ones = sum(sum(v) for v in result)
        answer = f"{total_ones}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")