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
        N = int(input())
        M = int(input())
        parent = list(range(N + 1))


        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u


        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu != pv:
                parent[pv] = pu


        for _ in range(M):
            x = int(input())
            y = int(input())

            for i in range(x, y):
                union(i, i + 1)
        unique = set()
        for i in range(1, N + 1):
            unique.add(find(i))
        answer = len(unique)
        answers.append(f"{answer}")
    print(*answers, sep="\n")