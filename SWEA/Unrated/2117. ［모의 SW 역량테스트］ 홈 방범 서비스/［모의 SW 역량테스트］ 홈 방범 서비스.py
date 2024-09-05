from itertools import product

INF = 10 ** 18
t = int(input())
answers = []
for hh in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    profit = [[[-(k ** 2 + (k - 1) ** 2) if k > 0 else -INF for _ in range(n)] for _ in range(n)] for k in
              range(2 * n + 2)]
    house_in_area = [[[0 for _ in range(n)] for _ in range(n)] for k in range(2 * n + 2)]
    for i in range(1, 2 * n + 2):
        for x1, y1, x2, y2 in product(range(n), repeat=4):
            if abs(x1 - x2) + abs(y1 - y2) <= i - 1:
                profit[i][y1][x1] += grid[y2][x2] * m
                house_in_area[i][y1][x1] += grid[y2][x2]
    profitable_pairs = [(k, y, x) for k, y, x in product(range(1, 2 * n + 2), range(n), range(n)) if
                        profit[k][y][x] >= 0]
    answer = max(house_in_area[k][y][x] for k, y, x in profitable_pairs)
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
