# 31067 다오의 경주 대회

N, K = map(int, input().split())
A = list(map(int, input().split()))
can_be_completed = True
result = 0
for i, v in enumerate(A):
    if i == 0:
        continue
    if A[i - 1] >= v + K:
        can_be_completed = False
        break
    if v <= A[i - 1] < v + K:
        result += 1
        A[i] += K
print(result if can_be_completed else -1)