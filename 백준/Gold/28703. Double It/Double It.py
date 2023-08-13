# 28703 Double It

# 원소의 최솟값을 계속적으로 확인하기 위해 우선순위 큐 선언
from heapq import heapify, heappop, heappush

N = int(input())
A = list(map(int, input().split(" ")))
original_max = max(A)
current_max = max(A)
heapify(A)
current_min = A[0]
result = current_max - current_min
# 어차피 이 이상은 최대와 최소의 차이를 더 키울 뿐이니 적당히 여기서 컷오프
while current_min < original_max:
    v = heappop(A)
    v *= 2
    current_max = max(current_max, v)
    heappush(A, v)
    current_min = A[0]
    result = min(result, current_max - current_min)
print(result)