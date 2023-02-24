# 2568 전깃줄 - 2
from bisect import bisect_left
from sys import stdin

wires_count: int = int(input())
A_wires_connections: list[int] = [0 for i in range(500000 + 1)]
A_wires_list: list[int] = []
for _ in range(wires_count):
    a_sub, b_sub = list(map(int, stdin.readline().strip().split(" ")))
    A_wires_connections[b_sub] = a_sub
    A_wires_list.append(a_sub)
A_wires_list.sort()

# 주어진 배열로 만들 수 있는 길이 i+1의 LIS index
dp_tail: list[int] = [0] * 500001
# LIS의 전에 있던 아이템들을 저장
dp_prev: list[int] = [-1] * 500001
# Find the index j of the largest element in dp[:lis_len] such that arr[dp[j]] < arr[i]
# 제일 적은 원소 순서대로 아이템 정렬해두기
lis_item_list: list[int] = []
lis_len: int = 0
lis: list[int] = []
wires_to_remove: list[int] = []

for i, j in enumerate(A_wires_connections):
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
    elif j < A_wires_connections[dp_tail[k]]:
        dp_tail[k] = i
        lis_item_list[k] = j
        dp_prev[i] = dp_tail[k - 1] if j > 0 else -1

# 맨 마지막 원소 불러오기
p: int = dp_tail[lis_len - 1]
# dp_prev가 LIS의 전의 아이템들을 저장해두고 있으니 그에 따라 LIS를 구성
while p != -1:
    lis.append(A_wires_connections[p])
    p = dp_prev[p]
lis.reverse()

print(wires_count - lis_len + 1)
for i, j in enumerate(A_wires_list):
    if j not in lis and j != 0:
        wires_to_remove.append(j)
print(*wires_to_remove, sep="\n")
