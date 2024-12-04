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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        matrix = [[int(input()) for _ in range(N)] for _ in range(N)]
        trace = 0
        repeated_rows = 0
        repeated_cols = 0
        for i in range(N):
            trace += matrix[i][i]
            if len(set(matrix[i])) != N:
                repeated_rows +=1
        for j in range(N):
            col = [matrix[i][j] for i in range(N)]
            if len(set(col)) != N:
                repeated_cols +=1
        answer = f"Case #{hh}: {trace} {repeated_rows} {repeated_cols}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")