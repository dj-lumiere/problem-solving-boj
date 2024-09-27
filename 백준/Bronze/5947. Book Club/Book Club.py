from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal

with open(0, 'r') as f:
    tokens = iter(f.read().split())
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
    for hh in range(1, t + 1):
        N = int(input())
        NQ = int(input())
        P = int(input())
        cow_responses = []
        for _ in range(N):
            cow_responses.append([int(input()) for _ in range(NQ)])
        conditions = []
        for _ in range(P):
            question = int(input())
            response = int(input())
            conditions.append((question, response))
        answer = 0
        for cow in cow_responses:
            match = True
            for question, response in conditions:
                if cow[question - 1] != response:
                    match = False
                    break
            if match:
                answer += 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")
