# 1389 케빈 베이컨의 6단계 법칙

from collections import deque
import math

user, node = list(map(int, input().split(" ")))
graph = {i: [] for i in range(1, user + 1)}
for _ in range(node):
    i, j = list(map(int, input().split(" ")))
    graph[i].append(j)
    graph[j].append(i)


def sol(user: int, graph: dict[int, list[int]]):
    kevin_bacon_number = dict()
    for i in range(1, user + 1):
        kevin_bacon_number[i] = [0 for i in range(0, user + 1)]
    for i in range(1, user + 1):
        for j in range(1, user + 1):
            if kevin_bacon_number[i][j] == 0 and i != j:
                i_j = bfs_length(i, j)
                kevin_bacon_number[i][j] = i_j
                kevin_bacon_number[j][i] = i_j
    max_number = math.inf
    answer = 0
    for i in range(1, user + 1):
        kevin_bacon_number_sum = sum(kevin_bacon_number[i])
        if max_number > kevin_bacon_number_sum:
            max_number, answer = kevin_bacon_number_sum, i
    print(answer)


def bfs_length(i, j) -> int:
    queue = deque()
    queue.append((i, 0))
    while queue:
        x, y = queue.popleft()
        if x == j:
            queue.clear()
            return y
        for i in graph[x]:
            queue.append((i, y + 1))


sol(user, graph)