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
        K = int(input())
        J = int(input())
        T = int(input())
        D = int(input())
        if K == 0 and J == 0 and T == 0 and D == 0:
            break
        S_min = max(J - 0.5, 0) * 9 + max(T - 0.5, 0) * 4 + max(D - 0.5, 0) * 4
        S_max = (J + 0.5) * 9 + (T + 0.5) * 4 + (D + 0.5) * 4
        if S_min < K < S_max:
            answer = "yes"
        else:
            answer = "no"
        answers.append(f"{answer}")
    print(*answers, sep="\n")