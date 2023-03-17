# 12852 1로 만들기 2

from collections import deque

N = int(input())
path_length = [0, 0, 1, 1] + [N + 1 for i in range(N - 3)]
path_tail = [0, 0, 1, 1] + [0 for i in range(N - 3)]
bfs_deque: deque[tuple[int, int, int]] = deque()
bfs_deque.append((2, 1, 1))
bfs_deque.append((3, 1, 1))

while bfs_deque:
    next_n, length_sub, path_tail_sub = bfs_deque.popleft()
    if next_n == N:
        break
    else:
        if next_n + 1 <= N and length_sub + 1 < path_length[next_n + 1]:
            path_length[next_n + 1] = length_sub + 1
            path_tail[next_n + 1] = next_n
            bfs_deque.append((next_n + 1, length_sub + 1, next_n))
        if next_n * 2 <= N and length_sub + 1 < path_length[next_n * 2]:
            path_length[next_n * 2] = length_sub + 1
            path_tail[next_n * 2] = next_n
            bfs_deque.append((next_n * 2, length_sub + 1, next_n))
        if next_n * 3 <= N and length_sub + 1 < path_length[next_n * 3]:
            path_length[next_n * 3] = length_sub + 1
            path_tail[next_n * 3] = next_n
            bfs_deque.append((next_n * 3, length_sub + 1, next_n))
path = [N]
path_follower_sub = N
while path_follower_sub:
    path.append(path_tail[path_follower_sub])
    path_follower_sub = path_tail[path_follower_sub]
path.pop()
print(path_length[N])
print(*path)
