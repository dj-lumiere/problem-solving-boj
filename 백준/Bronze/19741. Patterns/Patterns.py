from collections import deque
from itertools import product
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
        n = int(input())
        k = int(input())
        grid = [["." for _ in range(n)] for _ in range(n)]
        for i, j in product(range(n), repeat=2):
            num = i * n + j + 1  # The number in the (i, j) cell
            count = 0
            for a in range(1, int(num ** 0.5) + 1):
                if num % a == 0:
                    count += 1
                    if a != num // a:
                        count += 1
            if count <= k:
                grid[i][j] = "*"
        answers.append("\n".join("".join(v) for v in grid))
    print(*answers, sep="\n")