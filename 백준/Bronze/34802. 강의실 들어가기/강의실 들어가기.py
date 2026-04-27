from sys import stderr, stdout
from heapq import heappop, heappush

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        h1 = input()
        s1 = int(h1[:2]) * 3600 + int(h1[3:5]) * 60 + int(h1[6:])
        h2 = input()
        s2 = int(h2[:2]) * 3600 + int(h2[3:5]) * 60 + int(h2[6:])
        t1 = int(input())
        k = int(input())
        if s2 >= t1 * (100 - k) // 100 + s1:
            answers.append(1)
        else:
            answers.append(0)
    print(*answers, sep="\n")