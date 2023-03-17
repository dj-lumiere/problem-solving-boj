# 16928 뱀과 사다리 게임
from heapq import heappop, heappush

N, M = list(map(int, input().split(" ")))
graph: list[list[int]] = [
    [i + j for j in range(1, 6 + 1) if i + j <= 100] if i != 0 else []
    for i in range(100 + 1)
]
skip_pos = [False for i in range(101)]
skip_dst_pos = [False for i in range(101)]
visited = [False if i != 0 else True for i in range(100 + 1)]
visited[0] = True
visited[1] = True
for i in range(N + M):
    x, y = list(map(int, input().split(" ")))
    graph[x].clear()
    graph[x].append(y)
    skip_pos[x] = True
    skip_dst_pos[y] = True
bfs_heap = []
heappush(bfs_heap, (0, 1, []))
answer: int = 100
while bfs_heap:
    number_of_movement_without_skip_sub, position_sub, path = heappop(bfs_heap)
    if position_sub == 100:
        answer = number_of_movement_without_skip_sub
        break
    for i in graph[position_sub]:
        if skip_pos[position_sub]:
            heappush(
                bfs_heap,
                (number_of_movement_without_skip_sub, i, path + [i]),
            )
        elif not visited[i]:
            if i != 100 and not skip_dst_pos[i]:
                visited[i] = True
            heappush(
                bfs_heap,
                (number_of_movement_without_skip_sub + 1, i, path + [i]),
            )
print(answer)