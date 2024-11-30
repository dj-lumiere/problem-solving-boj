from math import gcd, isqrt
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        a, b = int(input()), int(input())
        gcd_ab = gcd(a, b)
        divisors = []
        for i in range(1, int(isqrt(gcd_ab)) + 1):
            if gcd_ab % i == 0:
                divisors.append(i)
                if i != gcd_ab // i:
                    divisors.append(gcd_ab // i)
        divisors.sort()
        for k in divisors:
            answer = f"{k} {a // k} {b // k}"
            answers.append(f"{answer}")
    print(*answers, sep="\n")