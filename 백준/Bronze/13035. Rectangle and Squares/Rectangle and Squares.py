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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        A, B, C = int(input()), int(input()), int(input())
        phil_area = A * B
        square_area = C * C
        k1 = max(1, phil_area // square_area) * square_area
        k2 = max(1, phil_area // square_area + 1) * square_area
        if abs(phil_area - k1) <= abs(phil_area - k2):
            answers.append(f"{k1}")
        else:
            answers.append(f"{k2}")
    print(*answers, sep="\n")