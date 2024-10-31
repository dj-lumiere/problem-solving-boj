from fractions import Fraction
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    answers = []
    for hh in range(t):
        n_token = input()
        if n_token is None:
            break
        n, x = int(n_token), float(input())
        amplitudes = []
        sum_sq = 0.0
        all_zero = True
        for _ in range(n):
            a = float(input())
            amplitudes.append(a)
            sum_sq += a * a
            if a != 0:
                all_zero = False
        if all_zero:
            for a in amplitudes:
                answer = f"{a:.10f}"
                answers.append(answer)
        else:
            avg_sq = sum_sq / n
            if avg_sq == 0:
                c = 0.0
            else:
                c = (x / avg_sq) ** 0.5
            for a in amplitudes:
                scaled = a * c
                answer = f"{scaled:.10f}"
                answers.append(answer)
    print(*answers, sep=" ")