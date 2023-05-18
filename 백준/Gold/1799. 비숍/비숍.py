# 1799 비숍

from typing import Callable
from functools import lru_cache
from sys import stdin

# 일단 대각선 방향으로는 놓으면 안 됨.
# 놓을 수 없는 자리에 놓으면 안 됨.

N: int = int(stdin.readline().strip())
available_diag_ld_list_for_black: int = (1 << (2 * N + 1)) - 1
available_diag_rd_list_for_black: int = (1 << (2 * N + 1)) - 1
available_diag_ld_list_for_white: int = (1 << (2 * N + 1)) - 1
available_diag_rd_list_for_white: int = (1 << (2 * N + 1)) - 1
graph: list[list[int]] = [
    list(map(int, stdin.readline().strip().split(" "))) for _ in range(N)
]
diag_ld: Callable[[int, int], int] = lambda pos_x, pos_y: pos_x + pos_y
diag_rd: Callable[[int, int], int] = lambda pos_x, pos_y: pos_y - pos_x + N - 1
answer: int = 0


@lru_cache(maxsize=None)
def is_safe(pos_x: int, pos_y: int, diag_ld_list: int, diag_rd_list: int):
    return (
        0 <= pos_x < N
        and 0 <= pos_y < N
        and graph[pos_y][pos_x]
        and (diag_ld_list & (1 << (diag_ld(pos_x, pos_y))))
        and (diag_rd_list & (1 << (diag_rd(pos_x, pos_y))))
    )


@lru_cache(maxsize=None)
def bishop_max_counter(
    pos_x: int,
    pos_y: int,
    answer_sub: int,
    diag_ld_list: int,
    diag_rd_list: int,
) -> int:
    if pos_x >= N:
        pos_y += 1
        pos_x = (pos_x ^ 1) % 2
    if pos_y >= N:
        return answer_sub
    result = answer_sub
    if is_safe(pos_x, pos_y, diag_ld_list, diag_rd_list):
        diag_ld_list ^= (1 << (diag_ld(pos_x, pos_y)))
        diag_rd_list ^= (1 << (diag_rd(pos_x, pos_y)))
        result = max(
            result,
            bishop_max_counter(
                pos_x=pos_x + 2,
                pos_y=pos_y,
                answer_sub=answer_sub + 1,
                diag_ld_list=diag_ld_list,
                diag_rd_list=diag_rd_list,
            ),
        )
        diag_ld_list ^= (1 << (diag_ld(pos_x, pos_y)))
        diag_rd_list ^= (1 << (diag_rd(pos_x, pos_y)))
    result = max(
        result,
        bishop_max_counter(
            pos_x=pos_x + 2,
            pos_y=pos_y,
            answer_sub=answer_sub,
            diag_ld_list=diag_ld_list,
            diag_rd_list=diag_rd_list,
        ),
    )
    return result


answer1: int = bishop_max_counter(
    pos_x=0,
    pos_y=0,
    answer_sub=0,
    diag_ld_list=available_diag_ld_list_for_black,
    diag_rd_list=available_diag_rd_list_for_black,
)
answer2: int = bishop_max_counter(
    pos_x=1,
    pos_y=0,
    answer_sub=0,
    diag_ld_list=available_diag_ld_list_for_white,
    diag_rd_list=available_diag_rd_list_for_white,
)
print(answer1 + answer2)
