from os import write

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for hh in range(t):
        n = int(input())
        m = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        acc_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i1, v1 in enumerate(grid, start=1):
            for i2, v2 in enumerate(v1, start=1):
                acc_sum[i1][i2] = grid[i1 - 1][i2 - 1] + acc_sum[i1 - 1][i2] + acc_sum[i1][i2 - 1] - acc_sum[i1 - 1][
                    i2 - 1]
        row_sum = [acc_sum[i][-1] for i in range(n + 1)]
        col_sum = [acc_sum[-1][i] for i in range(n + 1)]
        row_sum = [j - i for i, j in zip(row_sum, row_sum[1:])]
        col_sum = [j - i for i, j in zip(col_sum, col_sum[1:])]
        for _ in range(m):
            r1, c1, r2, c2, v = [int(input()) for _ in range(5)]
            for i in range(r1, r2 + 1):
                row_sum[i - 1] += (c2 - c1 + 1) * v
            for i in range(c1, c2 + 1):
                col_sum[i - 1] += (r2 - r1 + 1) * v
        answer = [row_sum, col_sum]
        answers[hh] = "\n".join(" ".join(map(str, x)) for x in answer)
    print(answers)