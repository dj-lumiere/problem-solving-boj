from collections import Counter
from decimal import Decimal, getcontext
from math import gcd
from random import randint
from sys import setrecursionlimit, stdout, stderr

getcontext().prec = 90

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n, k = int(input()), int(input())
        a = [int(input()) for _ in range(n)]
        prefix_sum = [0]
        for i, v in enumerate(a):
            prefix_sum.append(prefix_sum[-1] + v)
        prefix_sum_count = Counter(prefix_sum)
        answer = 0
        for v in prefix_sum[:-1]:
            prefix_sum_count[v] -= 1
            target = k + v
            sub_count = prefix_sum_count.get(target, 0)
            answer += sub_count
        answers.append(answer)
    print(*answers, sep="\n")
