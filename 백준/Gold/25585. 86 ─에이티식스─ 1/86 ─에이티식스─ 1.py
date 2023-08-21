# 25585 86 -에이티식스- 1

from itertools import permutations, product


def distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    x1, y1 = pos1
    x2, y2 = pos2
    return max(abs(x2 - x1), abs(y2 - y1))


def is_approachable(pos1: tuple[int, int], pos2: tuple[int, int]) -> bool:
    x1, y1 = pos1
    x2, y2 = pos2
    return (x1 + y1) % 2 == (x2 + y2) % 2


def can_eliminate_all_enemies(
    initial_pos: tuple[int, int], enemy_list: list[tuple[int, int]]
) -> bool:
    return all(is_approachable(initial_pos, i) for i in enemy_list)


def find_moving_distance(
    initial_pos: tuple[int, int], enemy_list: tuple[tuple[int, int]]
) -> int:
    current_pos = initial_pos
    result = 0
    for enemy_pos in enemy_list:
        result += distance(current_pos, enemy_pos)
        current_pos = enemy_pos
    return result


def find_minimum_distance(
    initial_pos: tuple[int, int], enemy_list: list[tuple[int, int]]
) -> int:
    if not can_eliminate_all_enemies(initial_pos, enemy_list):
        return -1
    result = 30000000
    for enemy_order in permutations(enemy_list):
        result = min(result, find_moving_distance(initial_pos, enemy_order))
    return result


grid_size: int = int(input())
grid_sprite: list[list[int]] = [
    list(map(int, input().split(" "))) for _ in range(grid_size)
]
initial_pos: tuple[int, int] = (0, 0)
enemy_list: list[tuple[int, int]] = []
for x, y in product(range(grid_size), repeat=2):
    if grid_sprite[y][x] == 2:
        initial_pos = (x, y)
    elif grid_sprite[y][x] == 1:
        enemy_list.append((x, y))
result: int = find_minimum_distance(initial_pos, enemy_list)
if result == -1:
    print("Shorei")
else:
    print(f"Undertaker\n{result}")