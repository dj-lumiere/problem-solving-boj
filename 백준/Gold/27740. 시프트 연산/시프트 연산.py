# B번 - 시프트 연산

from collections import deque

N: int = int(input())
A: list[int] = list(map(int, input().split(" ")))[::-1]
A_to_value: int = sum([j * 2**i for (i, j) in enumerate(A)])
visited: dict[int, bool] = dict()

bfs_deque: deque[tuple[int, int, str]] = deque()
bfs_deque.append((0, A_to_value, ""))
while bfs_deque:
    number_of_moves, number, path = bfs_deque.popleft()
    visited[number] = True
    if number == 0:
        print(number_of_moves)
        print(path)
        break
    else:
        if number >> 1 not in visited:
            visited[number >> 1] = True
            bfs_deque.append((number_of_moves + 1, number >> 1, path + "R"))
        if number << 1 not in visited:
            visited[number << 1 & (2**N - 1)] = True
            bfs_deque.append(
                (number_of_moves + 1, number << 1 & (2**N - 1), path + "L")
            )