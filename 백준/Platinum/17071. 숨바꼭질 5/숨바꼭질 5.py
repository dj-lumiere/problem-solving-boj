# 17071 숨바꼭질 5

from collections import deque, namedtuple
from typing import Callable, NamedTuple

sibling_pos: Callable[[int, int], int] = lambda K, t: K + t * (t + 1) // 2
mov_left: Callable[[int], int] = lambda x: x - 1
mov_right: Callable[[int], int] = lambda x: x + 1
warp: Callable[[int], int] = lambda x: 2 * x
x_limit: int = 500000
visited: list[list[bool]] = [[False] * 2 for _ in range(x_limit + 1)]


def hide_n_seek(N: int, K: int) -> int:
    if N == K:
        return 0
    else:
        bfs_deque: deque[tuple[int, int]] = deque()
        bfs_deque.append((0, N))
        visited[N][0] = True
        while bfs_deque:
            time, subin_pos = bfs_deque.popleft()
            next_time = time + 1
            for next_subin_pos in [
                mov_left(subin_pos),
                mov_right(subin_pos),
                warp(subin_pos),
            ]:
                if (
                    0 <= next_subin_pos <= x_limit
                    and not visited[next_subin_pos][next_time % 2]
                ):
                    visited[next_subin_pos][next_time % 2] = True
                    bfs_deque.append((next_time, next_subin_pos))
            next_sibling_pos = sibling_pos(K, next_time)
            if next_sibling_pos > x_limit:
                return -1
            elif visited[next_sibling_pos][next_time % 2]:
                return next_time
        return -1


print(hide_n_seek(*list(map(int, input().split(" ")))))