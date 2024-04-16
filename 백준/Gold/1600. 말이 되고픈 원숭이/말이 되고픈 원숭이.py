import os
from array import array
from collections import deque
from itertools import product


def is_inbound(pos_x, x_size, pos_y, y_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for a in range(t):
        k = int(input())
        w, h = int(input()), int(input())
        visited = [[[-1 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
        grid = [[int(input()) for _ in range(w)] for _ in range(h)]
        queue = deque([(0, 0, 0)])
        visited[0][0][0] = 0
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        special = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        while queue:
            cur_x, cur_y, cur_special = queue.popleft()
            for dx, dy in delta:
                next_x, next_y = cur_x + dx, cur_y + dy
                if not is_inbound(next_x, w, next_y, h):
                    continue
                if visited[next_y][next_x][cur_special] != -1:
                    continue
                if grid[next_y][next_x] == 1:
                    continue
                visited[next_y][next_x][cur_special] = visited[cur_y][cur_x][cur_special] + 1
                queue.append((next_x, next_y, cur_special))
            if cur_special >= k:
                continue
            for dx, dy in special:
                next_x, next_y, next_special = cur_x + dx, cur_y + dy, cur_special + 1
                if not is_inbound(next_x, w, next_y, h):
                    continue
                if visited[next_y][next_x][next_special] != -1:
                    continue
                if grid[next_y][next_x] == 1:
                    continue
                visited[next_y][next_x][next_special] = visited[cur_y][cur_x][cur_special] + 1
                queue.append((next_x, next_y, next_special))
        answer = [visited[-1][-1][i] for i in range(k + 1) if visited[-1][-1][i] != -1]
        answers[a] = f"{min(answer) if answer else -1}"
    print(answers)