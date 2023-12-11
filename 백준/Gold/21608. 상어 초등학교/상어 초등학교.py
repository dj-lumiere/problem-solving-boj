# 21608 상어 초등학교
from itertools import product


def is_inbound(row, col):
    return 0 <= row < N and 0 <= col < N


def find_space(grid, favorites, target):
    favorite_student_in_adjacent = [[0 for _ in range(N)] for _ in range(N)]
    blank_seat_in_adjacent = [[0 for _ in range(N)] for _ in range(N)]
    for row, col in product(range(N), repeat=2):
        if grid[row][col] != 0:
            continue
        for dx, dy in DELTA:
            nx, ny = col + dx, row + dy
            if not is_inbound(nx, ny):
                continue
            if grid[ny][nx] == 0:
                blank_seat_in_adjacent[row][col] += 1
                continue
            if grid[ny][nx] not in favorites[target]:
                continue
            favorite_student_in_adjacent[row][col] += 1
    # print(
    #     target,
    #     favorites[target],
    #     grid,
    #     favorite_student_in_adjacent,
    #     blank_seat_in_adjacent,
    # )
    max_favorite_student_in_adjacent = max(max(i) for i in favorite_student_in_adjacent)
    candidate_space = []
    for row, col in product(range(N), repeat=2):
        if grid[row][col] != 0:
            continue
        if favorite_student_in_adjacent[row][col] == max_favorite_student_in_adjacent:
            candidate_space.append((row, col))
    # print(candidate_space)
    max_blank_space = max(
        blank_seat_in_adjacent[row][col] for row, col in candidate_space
    )
    candidate_space2 = []
    for row, col in candidate_space:
        if blank_seat_in_adjacent[row][col] == max_blank_space:
            candidate_space2.append((row, col))
    candidate_space2.sort(key=lambda x: (x[0], x[1]))
    # print(candidate_space2)
    return candidate_space2[0]


def find_satisfaction_score(grid, favorites):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for row, col in product(range(N), repeat=2):
        favorite_student_count = 0
        target = grid[row][col]
        for dx, dy in DELTA:
            nx, ny = col + dx, row + dy
            if not is_inbound(nx, ny):
                continue
            if grid[ny][nx] not in favorites[target]:
                continue
            favorite_student_count += 1
        result[row][col] = [0, 1, 10, 100, 1000][favorite_student_count]
    # print(result)
    return sum(sum(i) for i in result)


N = int(input())
favorites = [[] for _ in range(N**2 + 1)]
target_order = []
for _ in range(N**2):
    target, *friend = map(int, input().split(" "))
    favorites[target] += list(friend)
    target_order.append(target)
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
grid = [[0 for _ in range(N)] for _ in range(N)]
for target in target_order:
    row, col = find_space(grid, favorites, target)
    grid[row][col] = target
print(find_satisfaction_score(grid, favorites))
