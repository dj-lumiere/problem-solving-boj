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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        x = [int(input()) for _ in range(n)]
        op_count = 0
        for i, (v1, v2) in enumerate(zip(x, x[1:])):
            while v1 >= v2:
                v2 *= 10
                op_count += 1
                possible_offset = 10 ** (len(str(v2)) - len(str(x[i + 1])))
                if v2 <= v1 < v2 + possible_offset - 1:
                    v2 = v1 + 1
                else:
                    continue
            else:
                x[i + 1] = v2
        answer = f"Case #{hh}: {op_count}"
        answers.append(answer)
    print(*answers, sep="\n")
