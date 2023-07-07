# 27440 1로 만들기 3

from collections import deque

N = int(input())
path_length = dict()
path_length[N] = 0
bfs_deque: deque[tuple[int, int]] = deque()
bfs_deque.append((N, 0))


def key_check(n: int) -> int:
    if n in path_length:
        return path_length[n]
    return 10**18


while bfs_deque:
    next_n, length_sub = bfs_deque.popleft()
    if next_n == 1:
        break
    else:
        if next_n - 1 > 0 and length_sub + 1 < key_check(next_n - 1):
            path_length[next_n - 1] = length_sub + 1
            bfs_deque.append((next_n - 1, length_sub + 1))
        if not next_n % 2 and length_sub + 1 < key_check(next_n // 2):
            path_length[next_n // 2] = length_sub + 1
            bfs_deque.append((next_n // 2, length_sub + 1))
        if not next_n % 3 and length_sub + 1 < key_check(next_n // 3):
            path_length[next_n // 3] = length_sub + 1
            bfs_deque.append((next_n // 3, length_sub + 1))
print(path_length[1])