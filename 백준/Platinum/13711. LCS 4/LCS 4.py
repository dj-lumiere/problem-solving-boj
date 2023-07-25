# 13711 LCS 4
from bisect import bisect_left

N: int = int(input())
A = list(map(int, input().split(" ")))
A_inv = [0] * N
for i, v in enumerate(A):
    A_inv[v - 1] = i
A = [i for i in range(1, N + 1)]
B = list(map(int, input().split(" ")))
B = [A_inv[v - 1] + 1 for v in B]

# 주어진 배열로 만들 수 있는 길이 i+1의 LIS index
dp_tail: list[int] = [0] * (N + 1)
# LIS의 전에 있던 아이템들을 저장
dp_prev: list[int] = [-1] * (N + 1)
# Find the index j of the largest element in dp[:lis_len] such that arr[dp[j]] < arr[i]
# 제일 적은 원소 순서대로 아이템 정렬해두기
lis_item_list: list[int] = []
lis_len: int = 0

for i, j in enumerate(B):
    # lis_item_list가 비어있거나, lis_item_list의 마지막 원소보다 더 큰 원소가 등장한 경우
    if not lis_item_list or lis_item_list[-1] < j:
        k = lis_len
        lis_item_list.append(j)
    # 아니면 lis_item_list에서 A[i]를 찾아서 index를 k에 저장
    else:
        k = bisect_left(lis_item_list, j)
    # 만약 k가 맨 마지막을 가르킨다면 lis_item_list에는 아이템 추가, dp_tail, dp_prev에는 아이템 갱신
    if k == lis_len:
        dp_tail[lis_len] = i
        lis_item_list[lis_len] = j
        dp_prev[i] = dp_tail[lis_len - 1] if lis_len > 0 else -1
        lis_len += 1
    # j가 A_wires[dp_tail[j]]보다 작다면 dp_tail이 갱신될 필요가 있음
    elif j < B[dp_tail[k]]:
        dp_tail[k] = i
        lis_item_list[k] = j
        dp_prev[i] = dp_tail[k - 1] if j > 0 else -1

print(lis_len)