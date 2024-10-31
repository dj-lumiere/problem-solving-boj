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
    t = 1
    answers = []
    for hh in range(t):
        n, m = (int(input()) for _ in range(2))
        lights = [False] * n
        for _ in range(m):
            op, s, e = (int(input()) for _ in range(3))
            if op == 0:
                for i in range(s - 1, e):
                    lights[i] = not lights[i]
            else:
                count = sum(lights[s - 1:e])
                answer = f"{count}"
                answers.append(answer)
    print(*answers, sep="\n")