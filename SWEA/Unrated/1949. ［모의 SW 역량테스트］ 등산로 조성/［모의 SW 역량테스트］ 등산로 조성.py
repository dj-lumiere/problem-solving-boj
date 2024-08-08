from collections import deque
from itertools import product


def find_distance(grid, is_inbound):
    answer_sub2 = -10 ** 9
    highest = max(max(v) for v in grid)
    starting_point = [(x2, y2) for x2, y2 in product(range(n), repeat=2) if grid[y2][x2] == highest]
    for x2, y2 in starting_point:
        queue = deque([(x2, y2)])
        length = [[0 for _ in range(n)] for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        length[y2][x2] = 1
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in DELTA:
                nx, ny = cx + dx, cy + dy
                if not is_inbound(nx, n, ny, n):
                    continue
                if visited[ny][nx]:
                    continue
                if grid[ny][nx] < grid[cy][cx]:
                    length[ny][nx] = length[cy][cx] + 1
                    queue.append((nx, ny))
        answer_sub2 = max(answer_sub2, max(max(v) for v in length))
    return answer_sub2


is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
INF = 10 ** 18
MOD = 1_000_000_000
t = int(input())
answers = []
for hh in range(t):
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    highest = max(max(v) for v in grid)
    starting_point = [(x, y) for x, y in product(range(n), repeat=2) if grid[y][x] == highest]
    answer = find_distance(grid, is_inbound)
    for x, y, i in product(range(n), range(n), range(1, k + 1)):
        if len(starting_point) == 1 and (x, y) == starting_point[0]:
            continue
        grid[y][x] -= i
        if grid[y][x] < 0:
            grid[y][x] += i
            continue
        answer_sub = find_distance(grid, is_inbound)
        answer = max(answer, answer_sub)
        grid[y][x] += i
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
