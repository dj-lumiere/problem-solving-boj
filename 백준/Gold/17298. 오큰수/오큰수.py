# 17298 오큰수

N: int = int(input())
A: list[int] = list(map(int, input().split(" ")))
index_stack: list[int] = []
answer: list[int] = [-1 for _ in range(N)]
for (i, j) in enumerate(A):
    while index_stack and A[i] > A[index_stack[-1]]:
        index = index_stack.pop()
        answer[index] = j
    index_stack.append(i)

print(*answer)