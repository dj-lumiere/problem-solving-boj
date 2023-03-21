# 11286 절댓값 힙

from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline())
my_heap: list[tuple[int, bool]] = []
for _ in range(N):
    x = int(stdin.readline())
    if x == 0 and not my_heap:
        print(0)
    elif x == 0 and my_heap:
        number, is_positive = heappop(my_heap)
        if is_positive:
            print(number)
        else:
            print(-number)
    elif x < 0:
        heappush(my_heap, (-x, False))
    elif x > 0:
        heappush(my_heap, (x, True))