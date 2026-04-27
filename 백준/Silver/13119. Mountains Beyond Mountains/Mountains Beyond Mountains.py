import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        m = int(input())
        x = int(input())
        grid = [["." for _ in range(m)] for _ in range(n)]
        y = [int(input()) for _ in range(m)]
        for i, v in enumerate(y):
            for j in range(v):
                grid[-j - 1][i] = "#"
        for j in range(m):
            if grid[-x][j] == ".":
                grid[-x][j] = "-"
            else:
                grid[-x][j] = "*"
        for j in range(2, m, 3):
            for i in range(n - x, n):
                if grid[i][j] == ".":
                    grid[i][j] = "|"
        answer = "\n".join("".join(x) for x in grid)
        answers[h] = f"{answer}"
    print(answers)