from itertools import product
def is_inbound(pos_x, size_x, pos_y, size_y):
    return 0 <= pos_x < size_x and 0 <= pos_y < size_y


t = int(input())
INF = 10**18
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answers = []
for hh in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    group = [[0 for _ in range(n)] for _ in range(n)]
    group_min = [INF]
    group_element_count = [0]
    current_group = 1
    for r, c in product(range(n), repeat=2):
        if group[r][c]:
            continue
        stack = [(r, c)]
        group_min.append(INF)
        group_element_count.append(0)
        group[r][c] = current_group
        while stack:
            y, x = stack.pop()
            group_min[current_group] = min(group_min[current_group], grid[y][x])
            group_element_count[current_group] += 1
            for dy, dx in DELTA:
                ny, nx = y + dy, x + dx
                if not is_inbound(nx, n, ny, n):
                    continue
                if grid[y][x] + 1 != grid[ny][nx]:
                    continue
                group[ny][nx] = current_group
                stack.append((ny, nx))
        current_group += 1
    max_element_count = max(group_element_count)
    index = min(group_min[i] for i, v in enumerate(group_min) if group_element_count[i] == max_element_count)
    answers.append(f"#{hh + 1} {index} {max_element_count}")
print(*answers, sep="\n")
