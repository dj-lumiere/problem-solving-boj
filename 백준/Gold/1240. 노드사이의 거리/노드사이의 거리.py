# 1240 노드사이의 거리

from sys import stdin, setrecursionlimit

setrecursionlimit(200000)


n, m = map(int, stdin.readline().strip().split(" "))
parent_child_weighted_dict: dict[int, list[tuple[int, int]]] = {
    i: [] for i in range(1, n + 1)
}
deadend_indicator = 987654321098765432109876543210


def find_distance(start: int, end: int, visited: list[bool], distance: int) -> int:
    visited[start] = True
    if start == end:
        return distance
    answer_candidates = [
        find_distance(i, end, visited, distance + j)
        for i, j in parent_child_weighted_dict[start]
        if not visited[i]
    ]
    if not answer_candidates:
        return deadend_indicator
    else:
        return min(answer_candidates)


for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().strip().split(" "))
    parent_child_weighted_dict[a].append((b, c))
    parent_child_weighted_dict[b].append((a, c))
queries = [tuple(map(int, stdin.readline().strip().split(" "))) for _ in range(m)]
for i, j in queries:
    visited = [False for i in range(n + 1)]
    print(find_distance(start=i, end=j, visited=visited, distance=0))
