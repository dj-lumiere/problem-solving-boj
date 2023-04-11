# 1967 트리의 지름

from sys import stdin, setrecursionlimit
setrecursionlimit(200000)

n = int(stdin.readline().strip())
parent_child_weighted_dict: dict[int, list[tuple[int, int]]] = {
    i: [] for i in range(1, n + 1)
}
for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().strip().split(" "))
    parent_child_weighted_dict[a].append((b, c))
    parent_child_weighted_dict[b].append((a, c))

def dfs(node: int, visited: list[bool], distance: int) -> tuple[int, int]:
    visited[node] = True
    max_distance_point: tuple[int, int] = (node, distance)
    for next_node, weight in parent_child_weighted_dict[node]:
        if not visited[next_node]:
            farthest_node, farthest_distance = dfs(
                next_node, visited, distance + weight
            )
            if farthest_distance > max_distance_point[1]:
                max_distance_point = (farthest_node, farthest_distance)
    return max_distance_point

# 루트에서 제일 멀리 떨어진 노드 하나 잡기
visited: list[bool] = [False for i in range(n + 1)]
farthest_node, _ = dfs(1, visited, 0)

# 거기서 제일 멀리 가는 거리를 하나 찾기
visited: list[bool] = [False for i in range(n + 1)]
_, diameter = dfs(farthest_node, visited, 0)
print(diameter)