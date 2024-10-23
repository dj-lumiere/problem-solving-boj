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
        x0, n = int(input()), int(input())
        sequence = [x0]
        if x0.bit_count() < n:
            sequence = [-1]
        else:
            for i in reversed(range(x0.bit_length())):
                x_now = sequence[-1]
                if x_now & (1 << i):
                    sequence.append(x_now ^ (1 << i))
            sequence.pop(0)
            sequence.pop()
            sequence = sequence[:n - 1] + [0]
        answer = " ".join(map(str, sequence))
        answers.append(answer)
    print(*answers, sep="\n")
