# 13913 숨바꼭질 4

from collections import deque

N, K = list(map(int, input().split(" ")))


def bfs():
    if N == K:
        print(0)
        print(N)
    elif N > K:
        print(N - K)
        print(" ".join(map(str, range(N, K - 1, -1))))
    else:
        queue = deque()
        queue.append((0, N, [N]))
        visited = [0 for i in range(0, 100000 + 1)]
        while queue:
            y, x, path_list = queue.popleft()
            visited[x] = 1
            if x == K:
                shortest_time = y
                break
            else:
                if not visited[x - 1] and 0 <= x - 1:
                    queue.append((y + 1, x - 1, path_list + [x - 1]))
                if x + 1 <= 100000:
                    if not visited[x + 1]:
                        queue.append((y + 1, x + 1, path_list + [x + 1]))
                if 2 * x <= 100000:
                    if not visited[2 * x]:
                        queue.append((y + 1, 2 * x, path_list + [2 * x]))
        print(shortest_time)
        print(" ".join(map(str, path_list)))


bfs()