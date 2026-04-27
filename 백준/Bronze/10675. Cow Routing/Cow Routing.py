from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        A = int(input())
        B = int(input())
        N = int(input())
        min_cost = INF
        for _ in range(N):
            cost = int(input())
            num_cities = int(input())
            cities = [int(input()) for _ in range(num_cities)]
            if A in cities and B in cities:
                index_A = cities.index(A)
                index_B = cities.index(B)
                if index_A < index_B:
                    if cost < min_cost:
                        min_cost = cost
        if min_cost != INF:
            answer = min_cost
        else:
            answer = -1
        answers.append(f"{answer}")
    print(*answers, sep="\n")