from collections import deque
from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

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
    for hh in range(1, t + 1):
        N = int(input())
        K = int(input())
        M = int(input())
        people = deque(range(1, N + 1))
        direction = 1
        for i in range(1, N + 1):
            for j in range(K - 1):
                if direction > 0:
                    people.append(people.popleft())
                else:
                    people.appendleft(people.pop())
            else:
                if direction > 0:
                    answers.append(people.popleft())
                else:
                    answers.append(people.pop())
            if i % M == 0:
                direction *= -1
    print(*answers, sep="\n")