from collections import deque, Counter
from heapq import heappop, heappush
from itertools import product, permutations, combinations
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    for hh in range(t):
        n, k = (int(input()), int(input()))
        # kx-y의 값을 구하기
        dots = [(int(input()), int(input())) for _ in range(n)]
        offset_count = Counter([k * x - y for x, y in dots])
        answer = sum(x * (x - 1) for x in offset_count.values())
        answers.append(f"{answer}")
    print(*answers, sep="\n")
