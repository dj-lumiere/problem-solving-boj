# 13549 숨바꼭질 3
import heapq
from sys import maxsize

N, K = list(map(int, input().split(" ")))

def bfs():
    if N == K:
        return 0
    else:
        heap = []
        heapq.heappush(heap, (0, N))
        shortest_time = maxsize
        visited = [0 for i in range(0, 100000 + 1)]
        while heap:
            y, x = heapq.heappop(heap)
            visited[x] = 1
            if x == K:
                return y
            else:
                if not visited[x - 1] and 0 <= x - 1:
                    heapq.heappush(heap, (y + 1, x - 1))
                if x + 1 <= 100000:
                    if not visited[x + 1]:
                        heapq.heappush(heap, (y + 1, x + 1))
                if 2 * x <= 100000:
                    if not visited[2 * x]:
                        heapq.heappush(heap, (y, 2 * x))


print(bfs())