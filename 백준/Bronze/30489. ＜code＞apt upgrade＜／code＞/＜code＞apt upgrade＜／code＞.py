from decimal import Decimal
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
        n, m, k = (int(input()) for _ in range(3))
        s = [int(input()) for _ in range(n)]
        s_sorted = sorted(s, reverse=True)
        total_sum = sum(s_sorted)
        done_sum = sum(s_sorted[:m])
        remaining = min(k, n - m)
        done_sum += sum(s_sorted[m:m + remaining])
        percentage = (Decimal(done_sum) / Decimal(total_sum)) * Decimal(100)
        answer = f"{percentage}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")