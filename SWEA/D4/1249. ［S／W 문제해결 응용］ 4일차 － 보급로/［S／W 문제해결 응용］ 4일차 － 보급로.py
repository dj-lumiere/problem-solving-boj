from heapq import heappop, heappush

is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
INF = 10 ** 18
MOD = 1_000_000_000
t = int(input())
answers = []
for hh in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    minimum_recovery_time = [[INF for _ in range(n)] for _ in range(n)]
    minimum_recovery_time[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    while pq:
        recovery_time, x, y = heappop(pq)
        if minimum_recovery_time[y][x] < recovery_time:
            continue
        for dx, dy in DELTA:
            if not is_inbound(x + dx, n, y + dy, n):
                continue
            next_recovery_time = recovery_time + grid[y + dy][x + dx]
            if next_recovery_time < minimum_recovery_time[y + dy][x + dx]:
                minimum_recovery_time[y + dy][x + dx] = next_recovery_time
                heappush(pq, (next_recovery_time, x + dx, y + dy))
    answer = minimum_recovery_time[-1][-1]
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
