from math import isqrt
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
    for hh in range(t):
        n = int(input())
        k = int(input())
        pointing = [int(input()) for _ in range(n)]
        current = 0
        m = 1
        visited = {}
        while m <= INF:
            target = pointing[current]
            if target == k:
                answer = f"{m}"
                break
            if current in visited:
                answer = "-1"
                break
            visited[current] = m
            current = target
            m += 1
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")