from itertools import product
from sys import stdout, stderr


class Shark:
    def __init__(self, idx, speed, direction, size):
        self.idx = idx
        self.speed = speed
        self.direction = direction
        self.size = size

    def __repr__(self):
        return f"Shark #{self.idx} [speed={self.speed}, direction={self.direction}, size={self.size}]"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        R, C, M = (int(input()) for _ in range(3))
        grid = [[[] for _ in range(C)] for _ in range(R)]
        for i in range(M):
            r, c, s, d, z = (int(input()) for _ in range(5))
            grid[r - 1][c - 1].append(Shark(i, s, d - 1, z))
        sharks_caught = []
        for i in range(C):
            for r in range(R):
                if grid[r][i]:
                    sharks_caught.append(grid[r][i][0])
                    grid[r][i].clear()
                    break
            new_grid = [[[] for _ in range(C)] for _ in range(R)]
            for r, c in product(range(R), range(C)):
                if not grid[r][c]:
                    continue
                current_shark = grid[r][c].pop()
                new_r, new_c = r, c
                if current_shark.direction == 0:
                    if current_shark.speed < r:
                        new_r -= current_shark.speed
                    else:
                        turns, mod = divmod(current_shark.speed - r, R - 1)
                        turns += 1
                        if turns % 2 == 1:
                            current_shark.direction = 1
                            new_r = mod
                        else:
                            new_r = R - 1 - mod
                elif current_shark.direction == 1:
                    if current_shark.speed < R - 1 - r:
                        new_r += current_shark.speed
                    else:
                        turns, mod = divmod(current_shark.speed - (R - 1 - r), R - 1)
                        turns += 1
                        if turns % 2 == 1:
                            current_shark.direction = 0
                            new_r = R - 1 - mod
                        else:
                            new_r = mod
                elif current_shark.direction == 3:
                    if current_shark.speed < c:
                        new_c -= current_shark.speed
                    else:
                        turns, mod = divmod(current_shark.speed - c, C - 1)
                        turns += 1
                        if turns % 2 == 1:
                            current_shark.direction = 2
                            new_c = mod
                        else:
                            new_c = C - 1 - mod
                elif current_shark.direction == 2:
                    if current_shark.speed < C - 1 - c:
                        new_c += current_shark.speed
                    else:
                        turns, mod = divmod(current_shark.speed - (C - 1 - c), C - 1)
                        turns += 1
                        if turns % 2 == 1:
                            current_shark.direction = 3
                            new_c = C - 1 - mod
                        else:
                            new_c = mod
                new_grid[new_r][new_c].append(current_shark)
            grid = new_grid
            for r, c in product(range(R), range(C)):
                if not grid[r][c]:
                    continue
                grid[r][c] = [sorted(grid[r][c], key=lambda x: x.size, reverse=True)[0]]
        answer = sum(i.size for i in sharks_caught)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
