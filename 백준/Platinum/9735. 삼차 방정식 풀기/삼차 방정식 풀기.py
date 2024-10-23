from collections import Counter
from math import gcd
from random import randint
from sys import setrecursionlimit, stdout, stderr

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
        a, b, c, d = (int(input()) for _ in range(4))
        # ax^2+bx+c = -d/x
        root_list = []
        if d == 0:
            root_list.append(0)
        else:
            for i in range(1, 1000000 + 1):
                if d % i == 0:
                    if a * i ** 2 + b * i ** 1 + c == -d // i:
                        root_list.append(i)
                        break
                    elif a * i ** 2 + b * -i ** 1 + c == -d // (-i):
                        root_list.append(-i)
                        break
        a, b = a, b + a * root_list[-1]
        b, c = b, c + b * root_list[-1]
        c, d = c, d + c * root_list[-1]
        det = b ** 2 - 4 * a * c
        if det >= 0:
            root_list.append((-b - det ** .5) / (2 * a))
            root_list.append((-b + det ** .5) / (2 * a))
        root_list = list(set([i.__round__(5) for i in root_list]))
        root_list.sort()
        answers.append(" ".join(map(str, root_list)))
    print(*answers, sep="\n")
