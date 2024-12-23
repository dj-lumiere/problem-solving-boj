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
        n = int(input())
        if n % 2 == 0:
            answer = "I LOVE CBNU"
        else:
            grid = [["*" for _ in range(n)]] + [[" " for _ in range(n)] for _ in range((n + 1) // 2)]
            start = n // 2
            end = n // 2
            for i in range((n + 1) // 2):
                grid[i + 1][start] = grid[i + 1][end] = "*"
                start -= 1
                end += 1
            answer = "\n".join("".join(v).rstrip() for v in grid)
        answers.append(f"{answer}")
    print(*answers, sep="\n")