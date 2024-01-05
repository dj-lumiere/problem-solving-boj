# 17245 서버실

from itertools import product

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
total_pc_count = 0
for i, j in product(range(N), repeat=2):
    total_pc_count += grid[i][j]
start = -1
end = 10_000_001
while start + 1 < end:
    mid = (start + end) // 2
    active_pc_count = 0
    for i, j in product(range(N), repeat=2):
        active_pc_count += min(grid[i][j], mid)
    if active_pc_count * 2 >= total_pc_count:
        end = mid
    else:
        start = mid
print(end)
