# 16173 점프왕 쩰리 (Small) / 16174 점프왕 쩰리 (Large)

from collections import deque

# OB 안 됨
# (0, 0) 출발
# R, D만 가능
# (N-1, N-1) 도착하면 게임 끝
# graph[b][a]의 값이 속도가 됨.
# 가능하면 HaruHaru
# 불가능하면 Hing

N = int(input())

graph = [list(map(int, input().split(" "))) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
delta_list = [(1, 0), (0, 1)]


def bfs() -> str:
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        visited[y][x] = True
        if graph[y][x] == -1:
            return "HaruHaru"
        for i, j in delta_list:
            nx, ny = x + i * graph[y][x], y + j * graph[y][x]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[ny][nx]:
                queue.append((nx, ny))
    return "Hing"


print(bfs())
