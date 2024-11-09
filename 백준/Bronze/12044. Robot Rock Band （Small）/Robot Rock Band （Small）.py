from collections import defaultdict
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
    t = int(input())
    answers = []
    for hh in range(1, t+1):
        N, K = int(input()), int(input())
        A = [int(input()) for _ in range(N)]
        B = [int(input()) for _ in range(N)]
        C = [int(input()) for _ in range(N)]
        D = [int(input()) for _ in range(N)]
        count = 0
        xor_ab = defaultdict(int)
        for a in A:
            for b in B:
                xor_ab[a ^ b] +=1
        for c in C:
            for d in D:
                target = K ^ c ^ d
                if target in xor_ab:
                    count += xor_ab[target]
        answer = f"Case #{hh}: {count}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")