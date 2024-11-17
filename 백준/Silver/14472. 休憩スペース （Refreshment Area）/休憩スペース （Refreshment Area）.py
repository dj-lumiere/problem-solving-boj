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
        N, M, D = int(input()), int(input()), int(input())
        grid = [input() for _ in range(N)]
        count = 0
        for i in range(N):
            for j in range(M - D + 1):
                if all(grid[i][j + k] == '.' for k in range(D)):
                    count += 1
        for j in range(M):
            for i in range(N - D + 1):
                if all(grid[i + k][j] == '.' for k in range(D)):
                    count += 1
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")