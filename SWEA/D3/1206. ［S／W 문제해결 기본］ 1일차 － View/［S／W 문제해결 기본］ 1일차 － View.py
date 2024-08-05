from itertools import product

t = 10
answers = []
for hh in range(t):
    n = int(input())
    heights = [0, 0]+list(map(int, input().split()))+[0, 0]
    grid = [[False for _ in range(256)] for _ in range(n+4)]
    for i, v in enumerate(heights):
        for j in range(v):
            grid[i][j] = True
    answer = 0
    for i, j in product(range(2, n+2), range(256)):
        if not grid[i][j]:
            continue
        if any([grid[i-2][j],grid[i-1][j],grid[i+1][j],grid[i+2][j]]):
            continue
        answer += 1
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
