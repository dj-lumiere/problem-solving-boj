from decimal import Decimal
from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
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
    for _ in range(t):
        Sx = Sy = Sxx = Sxy = 0
        n = int(input())
        xis = []
        yis = []
        for i in range(1, n + 1):
            xi = int(input())
            yi = int(input())
            xis.append(xi)
            yis.append(yi)
            Sx += xi
            Sy += yi
            Sxx += xi * xi
            Sxy += xi * yi
        if Sx * Sx != n * Sxx:
            a_num = n * Sxy - Sx * Sy
            a_den = n * Sxx - Sx * Sx
            a2 = a_num / a_den
            b2 = (Sy - a2 * Sx) / n
            sum_sq = 0
            for j in range(n):
                xi = xis[j]
                yi = yis[j]
                sum_sq += (a2 * xi + b2 - yi) ** 2
            answer = f"{a2} {b2}"
            answers.append(f"{answer}")
        else:
            answers.append("EZPZ")
    print(*answers, sep="\n")