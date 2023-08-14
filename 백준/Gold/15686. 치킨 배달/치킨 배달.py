# 15686 치킨 배달
from itertools import product, combinations

INF = 10**9


def find_distance(node1: tuple[int, int], node2: tuple[int, int]) -> int:
    return sum(abs(i - j) for i, j in zip(node1, node2))


def find_chicken_distance(
    chicken_store_pos: tuple[tuple[int, int]], house_pos: list[tuple[int, int]]
) -> int:
    result = 0
    for house_pos_sub in house_pos:
        minimum_distance_sub = INF
        for chicken_store_pos_sub in chicken_store_pos:
            minimum_distance_sub = min(
                minimum_distance_sub,
                find_distance(house_pos_sub, chicken_store_pos_sub),
            )
        result += minimum_distance_sub
    return result


result = INF
N, M = map(int, input().split(" "))
grid = [list(map(int, input().split(" "))) for _ in range(N)]
house_pos: list[tuple[int, int]] = []
chicken_store_pos: list[tuple[int, int]] = []
for i, j in product(range(N), range(N)):
    if grid[i][j] == 1:
        house_pos.append((i, j))
    elif grid[i][j] == 2:
        chicken_store_pos.append((i, j))
for positions in combinations(chicken_store_pos, M):
    result = min(result, find_chicken_distance(positions, house_pos))
print(result)