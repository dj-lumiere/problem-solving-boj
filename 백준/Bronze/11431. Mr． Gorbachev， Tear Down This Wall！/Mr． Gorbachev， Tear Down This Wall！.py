from itertools import combinations
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = int(input())
    answers = []
    for hh in range(t):
        n, s, p = (int(input()) for _ in range(3))
        points = [(int(input()), int(input())) for _ in range(n+1)]
        total_length = 0
        for i in range(n):
            total_length += abs(points[i][0] - points[i+1][0]) + abs(points[i][1] - points[i+1][1])
        total_time = total_length * s
        time_hours = (total_time + p -1) // p
        answer = f"Data Set {hh+1}:\n{time_hours}\n"
        answers.append(f"{answer}")
    print(*answers, sep="\n")