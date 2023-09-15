# 2162 선분 그룹

from itertools import product
from collections import Counter


def sign(x):
    if not x:
        return 0
    return x // abs(x)


def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    return sign(x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3))


def has_crosspoint(
    x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int
):
    is_123_ccw = ccw(x1, y1, x2, y2, x3, y3)
    is_124_ccw = ccw(x1, y1, x2, y2, x4, y4)
    is_341_ccw = ccw(x3, y3, x4, y4, x1, y1)
    is_342_ccw = ccw(x3, y3, x4, y4, x2, y2)
    can_have_crosspoint = False
    if is_123_ccw * is_124_ccw <= 0 and is_341_ccw * is_342_ccw <= 0:
        can_have_crosspoint = True
    if (
        is_123_ccw * is_124_ccw == 0
        and is_341_ccw * is_342_ccw == 0
        and not (
            min(x1, x2) <= max(x3, x4)
            and min(x3, x4) <= max(x1, x2)
            and min(y1, y2) <= max(y3, y4)
            and min(y3, y4) <= max(y1, y2)
        )
    ):
        can_have_crosspoint = False
    return int(can_have_crosspoint)


N = int(input())
line_segments = [tuple(map(int, input().split(" "))) for _ in range(N)]
connection_graph = [[i] for i in range(N)]
groups = [0 for _ in range(N)]
for i, j in product(range(N), repeat=2):
    if i <= j:
        continue
    if has_crosspoint(*line_segments[i], *line_segments[j]):
        connection_graph[i].append(j)
        connection_graph[j].append(i)
group_count = 0
for i in range(N):
    if groups[i] != 0:
        continue
    group_count += 1
    stack = [i]
    while stack:
        current_node = stack.pop()
        for next_node in connection_graph[current_node]:
            if groups[next_node]:
                continue
            groups[next_node] = group_count
            stack.append(next_node)

print(group_count)
print(max(Counter(groups).values()))
