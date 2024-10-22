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
    for hh in range(1, t + 1):
        _ = input()
        if _ is None:
            break
        N, M = int(_), int(input())
        matrix = [[int(input()) for _ in range(N)] for _ in range(N)]
        best = None
        for i in range(N - M + 1):
            for j in range(N - M + 1):
                sub_matrix = [matrix[x][j:j + M] for x in range(i, i + M)]
                distinct = set(x for row in sub_matrix for x in row)
                distinct_sorted = sorted(distinct, reverse=True)
                candidate = (len(distinct_sorted), list(map(lambda x: -x, distinct_sorted)), i, j)
                if best is None or candidate < best:
                    best = candidate
        answer = f"{best[2] + 1} {best[3] + 1}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")