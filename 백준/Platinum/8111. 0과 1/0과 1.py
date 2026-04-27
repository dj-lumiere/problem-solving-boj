# 8112 0과 1 - 2

from collections import deque


def make_graph(n, last):
    visited = [False] * n
    bfs_deque = deque([1])
    visited[1] = True
    last[1] = [-1, 1]
    while bfs_deque:
        current_node = bfs_deque.popleft()
        next_node1 = (current_node * 10) % n
        next_node2 = (current_node * 10 + 1) % n
        if not visited[next_node1]:
            visited[next_node1] = True
            last[next_node1] = [current_node, 0]
            bfs_deque.append(next_node1)
        if not visited[next_node2]:
            visited[next_node2] = True
            last[next_node2] = [current_node, 1]
            bfs_deque.append(next_node2)
        if not all((next_node1, next_node2)):
            return


def find_path(last):
    current_node, current_direction = last[0]
    answer = ""
    while current_node != -1:
        answer += str(current_direction)
        current_node, current_direction = last[current_node]
    answer += "1"
    return answer[::-1]


def sol(n):
    if n == 1:
        return 1
    last = [[0, 0] for _ in range(n)]
    make_graph(n, last)
    return find_path(last)


T = int(input())
for _ in range(T):
    n = int(input())
    print(sol(n))