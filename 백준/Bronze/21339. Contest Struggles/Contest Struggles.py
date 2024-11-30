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
        n, k = int(input()), int(input())
        d, s = int(input()), int(input())
        total_sum = n * d
        solved_sum = k * s
        unsolved_sum = total_sum - solved_sum
        if 0 <= unsolved_sum <= (n - k) * 100:
            avg_unsolved = Decimal(unsolved_sum) / Decimal(n - k)
            answer = f"{avg_unsolved}"
        else:
            answer = "impossible"
        answers.append(f"{answer}")
    print(*answers, sep="\n")