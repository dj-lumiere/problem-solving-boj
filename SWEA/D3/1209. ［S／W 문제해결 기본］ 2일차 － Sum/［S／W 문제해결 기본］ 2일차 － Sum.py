from itertools import product

t = 10
INF = 10 ** 18
answers = []
for hh in range(t):
    a = int(input())
    n = 100
    grid = [list(map(int, input().split())) for _ in range(n)]
    answer = max(*(sum(grid[r]) for r in range(n)), *(sum(grid[r][c] for r in range(n)) for c in range(n)),
                 sum(grid[r][r] for r in range(n)), sum(grid[r][-r - 1] for r in range(n)))
    answers.append(f"#{a} {answer}")
print(*answers, sep="\n")
