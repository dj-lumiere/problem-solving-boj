from itertools import product


def is_inbound(pos_x, size_x, pos_y, size_y):
    return 0 <= pos_x < size_x and 0 <= pos_y < size_y


t = 10
DELTA = [(-1, 0), (1, 0), (0, -1)]
answers = []
for hh in range(t):
    a = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]
    stack = [(x, y) for x, y in product(range(100), repeat=2) if grid[y][x] == 2]
    answer = 0
    while stack:
        x, y = stack.pop()
        if y == 0:
            answer = x
            break
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if not is_inbound(nx, 100, ny, 100):
                continue
            if grid[ny][nx] != 1:
                continue
            grid[ny][nx] = 2
            stack.append((nx, ny))
            break
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
