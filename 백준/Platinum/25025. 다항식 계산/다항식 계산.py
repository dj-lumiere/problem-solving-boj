#25025 다항식 계산
N, P = map(int, input().split())
A = list(map(int, input().split()))
A.reverse()
print(A[0]%P)
A_reduced = [0]*P
for i, v in enumerate(A):
    A_reduced[i % (P-1)] += v
for x in range(1,P):
    p_power = [pow(x,i,P) for i in range(P)]
    answer = 0
    for v1, v2 in zip(A_reduced, p_power):
        answer += v1 * v2
        answer %= P
    print(answer)