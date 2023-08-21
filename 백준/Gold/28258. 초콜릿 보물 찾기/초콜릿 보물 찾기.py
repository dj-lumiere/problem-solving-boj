# 28258 초콜릿 보물 찾기
from itertools import product


def is_inbound(grid_size: tuple[int, int], current_pos: tuple[int, int]) -> bool:
    return all([0 <= pos < size for pos, size in zip(current_pos, grid_size)])


def query(position: tuple[int, int]) -> bool:
    print("?", *position, flush=True)
    result = int(input())
    return result


def find_another_part(position, grid_size):
    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pos_x, pos_y = position
    np_x, np_y = 0, 0
    DELTA_FEASIBLE = []
    for dx, dy in DELTA:
        if not is_inbound(grid_size, (pos_x + dx, pos_y + dy)):
            continue
        DELTA_FEASIBLE.append((dx, dy))
    LAST_DELTA = DELTA_FEASIBLE.pop()
    for dx, dy in DELTA_FEASIBLE:
        if not is_inbound(grid_size, (pos_x + dx, pos_y + dy)):
            continue
        result = query((pos_x + dx, pos_y + dy))
        if result:
            np_x, np_y = pos_x + dx, pos_y + dy
            break
    else:
        dx, dy = LAST_DELTA
        np_x, np_y = pos_x + dx, pos_y + dy
    return (np_x, np_y)


def find_treasure_box():
    queries_list, last_query = parse_query_list()
    treasure_box_pos_1 = last_query
    treasure_box_pos_2 = (-1, -1)
    for position in queries_list:
        result = query(position)
        if result:
            treasure_box_pos_1 = position
            treasure_box_pos_2 = find_another_part(position, (10, 10))
            break
    else:
        treasure_box_pos_2 = find_another_part(treasure_box_pos_1, (10, 10))
    return treasure_box_pos_1, treasure_box_pos_2


def parse_query_list():
    queries_list = [(i, j) for (i, j) in product(range(10), range(10)) if (i + j) % 2]
    in_square = []
    in_side = []
    in_corner = []
    for i, j in queries_list:
        if (i in [0, 9]) and (j in [0, 9]):
            in_corner.append((i, j))
        elif (i in [0, 9]) or (j in [0, 9]):
            in_side.append((i, j))
        else:
            in_square.append((i, j))
    queries_list = in_square + in_side + in_corner
    last_query = queries_list.pop()
    return queries_list, last_query


treasure_box_pos_1, treasure_box_pos_2 = find_treasure_box()
print("!", *treasure_box_pos_1, *treasure_box_pos_2, flush=True)