# 1697 숨바꼭질
from collections import deque

N, K = list(map(int, input().split(" ")))


def bfs():
    if N == K:
        return 0
    else:
        queue = deque()
        queue.append((N, 0))
        visited = [0 for i in range(0, 100000 + 1)]
        while queue:
            x, y = queue.popleft()
            visited[x] = 1
            if x == K:
                queue.clear()
                return y
            else:
                if not visited[x - 1] and 0 <= x - 1:
                    queue.append((x - 1, y + 1))
                if x + 1 <= 100000:
                    if not visited[x + 1]:
                        queue.append((x + 1, y + 1))
                if 2 * x <= 100000:
                    if not visited[2 * x]:
                        queue.append((2 * x, y + 1))


print(bfs())