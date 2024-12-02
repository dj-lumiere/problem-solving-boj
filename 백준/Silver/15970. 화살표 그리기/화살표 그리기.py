from collections import defaultdict
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
        N = int(input())
        points = []
        for _ in range(N):
            x, y = int(input()), int(input())
            points.append((x, y))
        color_points = defaultdict(list)
        for x, y in points:
            color_points[y].append(x)
        total_length = 0
        for color in color_points:
            sorted_x = sorted(color_points[color])
            for i in range(len(sorted_x)):
                if i == 0:
                    closest = sorted_x[1]
                elif i == len(sorted_x) - 1:
                    closest = sorted_x[-2]
                else:
                    left = sorted_x[i] - sorted_x[i - 1]
                    right = sorted_x[i + 1] - sorted_x[i]
                    if left <= right:
                        closest = sorted_x[i - 1]
                    else:
                        closest = sorted_x[i + 1]
                total_length += abs(sorted_x[i] - closest)
        answer = total_length
        answers.append(f"{answer}")
    print(*answers, sep="\n")