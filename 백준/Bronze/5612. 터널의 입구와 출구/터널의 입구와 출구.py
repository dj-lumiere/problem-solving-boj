from itertools import product
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
    t = 1
    answers = []
    for hh in range(t):
        n, m = (int(input()) for _ in range(2))
        max_cars = m
        current = m
        flag = True
        for _ in range(n):
            enter, exit = int(input()), int(input())
            current += enter - exit
            if current < 0:
                flag = False
                break
            if current > max_cars:
                max_cars = current
        answer = max_cars if flag else 0
        answers.append(f"{answer}")
    print(*answers, sep="\n")