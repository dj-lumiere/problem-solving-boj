# 2206 벽 부수고 이동하기

from collections import deque


def is_inbound(x_pos, x_size, y_pos, y_size) -> bool:
    return 0 <= x_pos < x_size and 0 <= y_pos < y_size


def bfs(visited, x_size, y_size, wall_break_max) -> int:
    bfs_deque = deque()
    bfs_deque.append((0, 0, 0))
    visited[0][0][0] = 1
    while bfs_deque:
        x, y, broken_walls = bfs_deque.popleft()
        if x + 1 == x_size and y + 1 == y_size:
            return visited[y][x][broken_walls]
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if not is_inbound(nx, x_size, ny, y_size):
                continue
            if graph[ny][nx] == 0 and visited[ny][nx][broken_walls] == 0:
                visited[ny][nx][broken_walls] = visited[y][x][broken_walls] + 1
                bfs_deque.append((nx, ny, broken_walls))
            elif broken_walls < wall_break_max and graph[ny][nx] == 1 and visited[ny][nx][broken_walls + 1] == 0:
                visited[ny][nx][broken_walls + 1] = visited[y][x][broken_walls] + 1
                bfs_deque.append((nx, ny, broken_walls + 1))
    return -1


N, M, K = list(map(int, input().split(" ")))
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(bfs(visited, M, N, K))