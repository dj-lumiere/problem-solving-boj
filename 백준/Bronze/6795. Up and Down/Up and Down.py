from itertools import product
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
        a, b, c, d, s = (int(input()) for _ in range(5))


        def displacement(forward, backward, steps):
            cycle = forward + backward
            full_cycles = steps // cycle
            remainder = steps % cycle
            return full_cycles * (forward - backward) + min(forward, remainder)


        nikky = displacement(a, b, s)
        byron = displacement(c, d, s)
        if nikky > byron:
            answer = "Nikky"
        elif byron > nikky:
            answer = "Byron"
        else:
            answer = "Tied"
        answers.append(f"{answer}")
    print(*answers, sep="\n")