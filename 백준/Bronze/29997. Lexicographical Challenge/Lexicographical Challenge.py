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
        S = input()
        K = int(input())
        groups = {}
        for i, c in enumerate(S):
            key = i % K
            if key in groups:
                groups[key].append(c)
            else:
                groups[key] = [c]
        for key in groups:
            groups[key].sort()
        result = list(S)
        indices = {key: 0 for key in groups}
        for i in range(len(S)):
            key = i % K
            result[i] = groups[key][indices[key]]
            indices[key] += 1
        answer = ''.join(result)
        answers.append(f"{answer}")
    print(*answers, sep="\n")