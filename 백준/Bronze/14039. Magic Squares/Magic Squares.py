import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    INF = 10 ** 18
    for h in range(t):
        grid = [int(input()) for _ in range(16)]
        row_sum = [sum(grid[j + i * 4] for j in range(4)) for i in range(4)]
        col_sum = [sum(grid[i + j * 4] for j in range(4)) for i in range(4)]
        if all(i == row_sum[0] for i in row_sum) and all(i == col_sum[0] for i in col_sum):
            answer = "magic"
        else:
            answer = "not magic"
        answers[h] = f"{answer}"
    print(answers)