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
    for hh in range(t):
        n = int(input())
        m = int(input())
        participants = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                participants[i].append(int(input()))
        D = participants[0]
        S1 = set()
        S2 = set()
        for j in range(m):
            if D[j] == 100:
                any_other = False
                for k in range(1, n):
                    if participants[k][j] == 100:
                        any_other = True
                        break
                if not any_other:
                    S1.add(j)
                else:
                    S2.add(j)
        if len(S1) > 0:
            answer = "1 1"
        elif len(S2) > 0:
            count = 0
            for i in range(n):
                flag = True
                for j in S2:
                    if participants[i][j] != 100:
                        flag = False
                        break
                if flag:
                    count += 1
            answer = f"1 {count}"
        else:
            answer = f"1 {n}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")