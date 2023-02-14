# 16953 A → B
from sys import setrecursionlimit
from collections import deque

A, B = list(map(int, input().split(" ")))
queue = deque()
queue.append((A, 1))


def bfs():
    while queue:
        x, y = queue.popleft()
        if x == B:
            return y
        else:
            if 2 * x <= B:
                queue.append((2 * x, y + 1))
            if 10 * x + 1 <= B:
                queue.append((10 * x + 1, y + 1))
    return -1


print(bfs())