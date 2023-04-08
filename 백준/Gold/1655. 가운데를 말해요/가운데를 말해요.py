# 1655 가운데를 말해요

from heapq import heappush, heappop
from sys import stdin, stdout

N = int(stdin.readline().strip())
A = [int(stdin.readline().strip()) for _ in range(N)]
min_heap: list[int] = []
max_heap: list[int] = []

for (h, i) in enumerate(A):

    if not h % 2:
        # min_heap에 아무 것도 없으면 일단 min_heap에 넣기
        if not min_heap:
            heappush(min_heap, i)
        else:
            # max heap 최댓값이 i보다 작으면 max heap에 있던 거 하나 빼고 그 자리에 i가 들어감
            if i < -max_heap[0]:
                heappush(min_heap, -heappop(max_heap))
                heappush(max_heap, -i)
            else:
                heappush(min_heap, i)
    else:
        # min heap 최솟값이 i보다 작으면 min heap에 있던 거 하나 빼고 그 자리에 i가 들어감
        if i > min_heap[0]:
            heappush(max_heap, -heappop(min_heap))
            heappush(min_heap, i)
        else:
            heappush(max_heap, -i)
    # 짝수개면 max_heap와 min_heap 중 비교
    if h % 2:
        stdout.write(f"{min(min_heap[0], -max_heap[0])}\n")
    # 홀수개면 min_heap에서
    else:
        stdout.write(f"{min_heap[0]}\n")
