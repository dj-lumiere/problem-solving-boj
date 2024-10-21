from itertools import product
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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        paper_count = [0, 0, 0]
        stack = [(n, 0, 0)]
        while stack:
            size, x_start, y_start = stack.pop()
            if size == 1:
                paper_count[grid[y_start][x_start]] += 1
                continue
            x_end, y_end = x_start + size, y_start + size
            plus_1_count = 0
            zero_count = 0
            minus_1_count = 0
            for j in range(y_start, y_end):
                for i in range(x_start, x_end):
                    if grid[j][i] == 1:
                        plus_1_count += 1
                    elif grid[j][i] == -1:
                        minus_1_count += 1
                    else:
                        zero_count +=1
            if plus_1_count == size * size:
                paper_count[1] += 1
            elif zero_count == size * size:
                paper_count[0] += 1
            elif minus_1_count == size * size:
                paper_count[-1] += 1
            else:
                for i, j in product(range(3), repeat=2):
                    stack.append((size // 3, x_start + size // 3 * i, y_start + size // 3 * j))
        answer = f"{paper_count[-1]}\n{paper_count[0]}\n{paper_count[1]}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")