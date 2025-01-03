from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr
from collections import deque

getcontext().prec = 30

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
    t = 1
    answers = []
    for hh in range(t):
        S = int(input())
        line = deque()
        next_cow = 1
        for _ in range(S):
            x = input()
            if x == 'A':
                y = input()
                if y == 'L':
                    line.appendleft(next_cow)
                else:
                    line.append(next_cow)
                next_cow += 1
            else:
                direction = input()
                K = int(input())
                if direction == 'L':
                    for _ in range(K):
                        line.popleft()
                else:
                    for _ in range(K):
                        line.pop()
        answer = '\n'.join(map(str, line))
        answers.append(f"{answer}")
    print(*answers, sep="\n")