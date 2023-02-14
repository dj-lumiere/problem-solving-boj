# 12851 숨바꼭질 2
from collections import deque

N, K = list(map(int, input().split(" ")))


def bfs():
    queue = deque()
    queue.append((N, 0))
    paths = 0
    shortest_time = 9999999999
    visited = [0 for i in range(0, 100000 + 1)]
    if N == K:
        print(0)
        print(1)
    else:
        while queue:
            x, y = queue.popleft()
            visited[x] =1
            if x == K:
                shortest_time = min(shortest_time, y)
                paths += 1
            if shortest_time != 0 and y > shortest_time:
                queue.clear()
            else:
                if not visited[x - 1] and 0 <= x - 1:
                    queue.append((x - 1, y + 1))
                if x + 1 <= 100000:
                    if not visited[x + 1]:
                        queue.append((x + 1, y + 1))
                if 2 * x <= 100000:
                    if not visited[2 * x]:
                        queue.append((2 * x, y + 1))
        print(shortest_time)
        print(paths)

bfs()