from bisect import bisect_left
from sys import stdout, stderr

with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answers = []
    INF = 10 ** 18
    t = int(input())
    for hh in range(t):
        a, b = map(int, input().split())
        movement_increase_threshold = [0]
        i = 1
        while True:
            x, y = i * i, i * i + i
            if x >= 2 ** 31:
                break
            i += 1
            movement_increase_threshold.append(x)
            if y >= 2 ** 31:
                continue
            movement_increase_threshold.append(y)
        answer = bisect_left(movement_increase_threshold, b - a)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
