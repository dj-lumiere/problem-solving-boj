from itertools import product
from sys import stdout, stderr



with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(t):
        win_loses = {}
        for _ in range(16):
            x, y, g1, g2 = input(), input(), int(input()), int(input())
            if x not in win_loses:
                win_loses[x] = [0,0]
            if y not in win_loses:
                win_loses[y] = [0,0]
            if g1 > g2:
                win_loses[x][0] += 1
                win_loses[y][1] += 1
            else:
                win_loses[x][1] += 1
                win_loses[y][0] += 1
        answer = [k for k, v in win_loses.items() if v == [4, 0]][0]
        answers.append(f"{answer}")
    print(*answers, sep="\n")
