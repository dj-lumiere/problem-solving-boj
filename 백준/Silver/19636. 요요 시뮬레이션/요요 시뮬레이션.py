from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from math import sqrt
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
        W0, I0, T = int(input()), int(input()), int(input())
        D, I, A = int(input()), int(input()), int(input())
        
        W1 = W0
        for _ in range(D):
            W1 += (I - (I0 + A))
            if W1 <= 0:
                answer = "Danger Diet"
                break
        else:
            answer = f"{W1} {I0}"
        answers.append(f"{answer}")
        
        W2 = W0
        BMR = I0
        for _ in range(D):
            energy_balance = I - (BMR + A)
            W2 += energy_balance
            if W2 <= 0 or BMR <= 0:
                answer = "Danger Diet"
                break
            if abs(energy_balance) > T:
                BMR += energy_balance // 2
            if W2 <= 0 or BMR <= 0:
                answer = "Danger Diet"
                break
        else:
            if BMR < I0:
                answer = f"{W2} {BMR} YOYO"
            else:
                answer = f"{W2} {BMR} NO"
        answers.append(f"{answer}")
    print(*answers, sep="\n")