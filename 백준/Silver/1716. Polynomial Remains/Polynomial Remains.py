from decimal import getcontext
from sys import stderr, stdout

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
    t = INF
    answers = []
    for hh in range(t):
        n, k = int(input()), int(input())
        if n == -1 and k == -1:
            break
        coefs = [int(input()) for _ in range(n + 1)]
        coefs.reverse()
        for i in range(n + 1 - k):
            coefs[i + k] -= coefs[i]
            coefs[i] = 0
        coefs.reverse()
        remainder = coefs[:k + 1]
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
        if all(c == 0 for c in remainder):
            answers.append("0")
        else:
            answers.append(' '.join(map(str, remainder)))
    print(*answers, sep="\n")