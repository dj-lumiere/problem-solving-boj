# 9019 DSLR
from collections import deque
from sys import stdin


N = int(input())
for _ in range(N):
    a, b = list(map(int, stdin.readline().strip().split(" ")))
    bfs_deque: deque[tuple] = deque()
    bfs_deque.append((a, ""))
    visited: list[bool] = [False for i in range(10000)]
    visited[a] = True
    while bfs_deque:
        next_num, path = bfs_deque.popleft()
        if next_num == b:
            print(path)
            bfs_deque.clear()
        else:
            d = next_num * 2 % 10000
            s = (next_num - 1) % 10000
            l1, l2 = divmod(next_num, 1000)
            r1, r2 = divmod(next_num, 10)
            l = l2 * 10 + l1
            r = r2 * 1000 + r1
            if next_num != 0 and not visited[d]:
                visited[d] = True
                bfs_deque.append((d, path + "D"))
            if not visited[s]:
                visited[s] = True
                bfs_deque.append((s, path + "S"))
            if (
                next_num != l
                and (not path or path[-1] != "R" or path[-3:] != "LLL")
                and not visited[l]
            ):
                visited[l] = True
                bfs_deque.append((l, path + "L"))
            if (
                next_num != r
                and (not path or path[-1] != "L" or path[-3:] != "RRR")
                and not visited[r]
            ):
                visited[r] = True
                bfs_deque.append((r, path + "R"))
