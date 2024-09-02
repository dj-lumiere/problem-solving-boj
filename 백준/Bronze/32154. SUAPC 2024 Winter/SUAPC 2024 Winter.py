from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    result = ['', '11 A B C D E F G H J L M',
              '9 A C E F G H I L M',
              '9 A C E F G H I L M',
              '9 A B C E F G H L M',
              '8 A C E F G H L M',
              '8 A C E F G H L M',
              '8 A C E F G H L M',
              '8 A C E F G H L M',
              '8 A C E F G H L M',
              '8 A B C F G H L M',
              ]
    for hh in range(1, t + 1):
        n = int(input())
        answer = result[n]
        answers.append(f"{answer}")
    print(*answers, sep="\n")
