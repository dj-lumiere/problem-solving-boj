answers = []
INF = 10 ** 18
t = 10
for hh in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    grid_transpose = [[grid[i][j] for i in range(n)] for j in range(n)]
    grid_transpose_remove_zero = [[v2 for v2 in v if v2 != 0] for v in grid_transpose]
    for i, v in enumerate(grid_transpose_remove_zero):
        start = 0
        end = len(v)
        for j, v2 in enumerate(v):
            if v2 == 1:
                start = j
                break
        for j, v2 in enumerate(reversed(v)):
            if v2 == 2:
                end = len(v) - j
                break
        grid_transpose_remove_zero[i] = v[start:end]
        if grid_transpose_remove_zero[i] == [1] or grid_transpose_remove_zero[i] == [2]:
            grid_transpose_remove_zero[i] = []
    answer = 0
    for i, v in enumerate(grid_transpose_remove_zero):
        remove_duplicate = []
        for j, v2 in enumerate(v):
            if not remove_duplicate:
                remove_duplicate.append(v2)
                continue
            if remove_duplicate[-1] == v2:
                continue
            remove_duplicate.append(v2)
        answer += len(remove_duplicate) // 2
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
