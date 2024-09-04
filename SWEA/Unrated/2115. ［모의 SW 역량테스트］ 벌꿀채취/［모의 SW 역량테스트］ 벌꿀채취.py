from itertools import product, combinations

t = int(input())
answers = []
for hh in range(1, t + 1):
    n, m, cc = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    max_honey = [[0 for _ in range(n - m + 1)] for _ in range(n)]
    for r, c in product(range(n), range(n - m + 1)):
        sub_honey = [grid[r][c + i] for i in range(m)]
        sub_profit = 0
        for mask in range(1, 1 << m):
            has_picked = [(mask & (1 << i) != 0) for i in range(m)]
            honey_picked = sum(i * j for i, j in zip(sub_honey, has_picked))
            if honey_picked > cc:
                continue
            sub_profit = max(sub_profit, sum(i * i * j for i, j in zip(sub_honey, has_picked)))
        max_honey[r][c] = sub_profit
    answer = 0
    for (r1, c1), (r2, c2) in combinations(product(range(n), range(n - m + 1)), r=2):
        if r1 == r2 and c1 + m > c2:
            continue
        answer = max(answer, max_honey[r1][c1] + max_honey[r2][c2])
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
