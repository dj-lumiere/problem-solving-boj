import os
from itertools import product
from fractions import Fraction


def is_inbound(x_pos, y_pos, width, height):
    return 0 <= x_pos < width and 0 <= y_pos < height


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        grid = [[int(input()) for _ in range(n)] for _ in range(n)]
        nouzen_position = [(i, j) for i, j in product(range(n), repeat=2) if grid[j][i] == 2][0]
        can_move = [[0 for _ in range(n)] for _ in range(n)]
        delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
        stack = [nouzen_position]
        can_move[nouzen_position[1]][nouzen_position[0]] = 1
        while stack:
            x, y = stack.pop()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if not is_inbound(nx, ny, n, n):
                    continue
                if can_move[ny][nx] == 1:
                    continue
                can_move[ny][nx] = 1
                stack.append((nx, ny))
        answers[h] = "Kiriya" if any(
            can_move[i][j] == grid[i][j] == 1 for i, j in product(range(n), repeat=2)) else "Lena"
    print(answers)