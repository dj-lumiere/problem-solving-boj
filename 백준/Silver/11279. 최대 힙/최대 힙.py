# 11279 최대 힙

from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline())
my_heap:list[int] = []
for _ in range(N):
    x = int(stdin.readline())
    if x == 0 and not my_heap:
        print(0)
    elif x == 0 and my_heap:
        print(-heappop(my_heap))
    else:
        heappush(my_heap, -x)