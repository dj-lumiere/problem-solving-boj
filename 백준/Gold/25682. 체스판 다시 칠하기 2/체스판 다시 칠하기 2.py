# 25682 체스판 다시 칠하기 2
from itertools import product


def find_accumulative_sum(accumulative_sum, pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    x1 += 1
    y1 += 1
    x2 += 1
    y2 += 1
    return (
        accumulative_sum[y2][x2]
        - accumulative_sum[y2][x1 - 1]
        - accumulative_sum[y1 - 1][x2]
        + accumulative_sum[y1 - 1][x1 - 1]
    )


def make_accumulative_sum(grid, x_size, y_size):
    result = [[0 for _ in range(x_size + 1)] for _ in range(y_size + 1)]
    for x, y in product(range(x_size), range(y_size)):
        result[y + 1][x + 1] = (
            result[y + 1][x] + result[y][x + 1] - result[y][x] + grid[y][x]
        )
    return result


def make_mispaint_grid(grid, x_size, y_size, *, even_color, odd_color):
    result = [[0 for _ in range(x_size)] for _ in range(y_size)]
    for x, y in product(range(x_size), range(y_size)):
        if (x + y) % 2 and grid[y][x] != odd_color:
            result[y][x] = 1
        elif not (x + y) % 2 and grid[y][x] != even_color:
            result[y][x] = 1
    return result


def find_mispaint_count(accumulative_sum, x_pos, y_pos, K):
    return find_accumulative_sum(
        accumulative_sum, (x_pos, y_pos), (x_pos + K - 1, y_pos + K - 1)
    )


def is_inbound(x_pos, y_pos, x_size, y_size):
    return 0 <= x_pos < x_size and 0 <= y_pos < y_size


def find_minimal_mispaint_count(grid, x_size, y_size, K):
    mispaint1_grid = make_mispaint_grid(
        grid, x_size, y_size, even_color="B", odd_color="W"
    )
    mispaint2_grid = make_mispaint_grid(
        grid, x_size, y_size, even_color="W", odd_color="B"
    )
    accumulative_sum1 = make_accumulative_sum(mispaint1_grid, x_size, y_size)
    accumulative_sum2 = make_accumulative_sum(mispaint2_grid, x_size, y_size)
    result = K * K + 1
    for x, y in product(range(x_size), range(y_size)):
        if not is_inbound(x + K - 1, y + K - 1, x_size, y_size):
            continue
        result_sub1 = find_mispaint_count(accumulative_sum1, x, y, K)
        result_sub2 = find_mispaint_count(accumulative_sum2, x, y, K)
        result = min(result, result_sub1, result_sub2)
    return result


N, M, K = map(int, input().split(" "))
grid = [list(input()) for _ in range(N)]
print(find_minimal_mispaint_count(grid, M, N, K))