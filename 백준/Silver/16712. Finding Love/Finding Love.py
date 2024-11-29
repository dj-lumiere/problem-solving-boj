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
        n, m = int(input()), int(input())
        A = [int(input()) for _ in range(n)]
        V = [int(input()) for _ in range(n - m + 1)]
        current = list(range(m))
        next_ptr = m
        for i in range(n - m + 1):
            Vi = V[i] - 1
            sorted_current = sorted(current, key=lambda j: (A[j], j))
            to_eliminate = sorted_current[Vi]
            current.remove(to_eliminate)
            if next_ptr < n:
                current.append(next_ptr)
                next_ptr += 1
        remaining = sorted([A[j] for j in current])
        answer = ' '.join(map(str, remaining))
        answers.append(f"{answer}")
    print(*answers, sep="\n")