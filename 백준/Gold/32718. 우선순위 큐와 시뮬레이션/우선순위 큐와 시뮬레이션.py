from bisect import bisect_left
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
        n, k, x = (int(input()) for _ in range(3))
        q = [int(input()) % k for _ in range(n)]
        q.sort()
        a = [int(input()) for _ in range(x)]
        current_number = 0
        for i in a:
            current_number += i
            current_number %= k
            target = -current_number % k
            answer = (q[bisect_left(q, target) - 1] + current_number) % k
            answers.append(answer)
    print(*answers, sep=" ")