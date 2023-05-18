# 9663 N-Queen

from collections import deque

# x좌표가 같아도 안 되고, y좌표가 같아도 안 되고, x+y가 같아도 안 되고 abs(x-y)가 같아도 안 됨

N: int = int(input())
global result
result = 0


def n_queen_solution_counter(
    n: int,
    col: int,
    rows: list[bool],
    diag_ld_list: list[bool],
    diag_rd_list: list[bool],
):
    if col == n:
        global result
        result += 1
    else:
        row = 0
        while row < n:
            diag_ld = col - row + n - 1
            diag_rd = col + row
            if not (rows[row] or diag_ld_list[diag_ld] or diag_rd_list[diag_rd]):
                rows[row] = True
                diag_ld_list[diag_ld] = True
                diag_rd_list[diag_rd] = True
                n_queen_solution_counter(n, col + 1, rows, diag_ld_list, diag_rd_list)
                rows[row] = False
                diag_ld_list[diag_ld] = False
                diag_rd_list[diag_rd] = False
            row += 1


def n_queen(n: int) -> int:
    if 1 < n < 4:
        return 0
    elif n == 1:
        return 1
    else:
        rows, diag_ld_list, diag_rd_list = (
            [False] * n,
            [False] * (2 * n - 1),
            [False] * (2 * n - 1),
        )
        n_queen_solution_counter(n, 0, rows, diag_ld_list, diag_rd_list)
        return result


print(n_queen(N))