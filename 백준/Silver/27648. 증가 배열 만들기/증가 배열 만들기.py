from collections import deque

N, M, K = list(map(int, input().split(" ")))
if K < N + M - 1:
    print("NO")
else:
    array: list[list[int]] = [[0 for x in range(M)] for y in range(N)]
    array[0][0] = 1
    bfs_deque: deque[tuple] = deque([(1, (0, 0))])
    dx_dy_list: list[tuple] = [(1, 0), (0, 1)]
    while bfs_deque:
        next_number, (x, y) = bfs_deque.popleft()
        for dx, dy in dx_dy_list:
            nx, ny = x + dx, y + dy
            if nx >= M or ny >= N:
                continue
            if not array[ny][nx]:
                array[ny][nx] = next_number + 1
                bfs_deque.append((next_number + 1, (nx, ny)))
    print("YES")
    for i in range(N):
        print(*array[i], sep=" ")