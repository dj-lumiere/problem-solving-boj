# 14888 연산자 끼워넣기

def permut(N: int, M: int) -> list[list[int]]:
    list_permut = []
    stack = []

    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            return
        else:
            # 순열
            for i in range(0, N):
                if i not in stack:
                    stack.append(i)
                    dfs(i, M - 1, stack)
                    stack.pop()

    dfs(0, M, stack)
    return list_permut


N = int(input())
A = list(map(int, input().split(" ")))
operator_count = list(map(int, input().split(" ")))
operator_count = operator_count
operator_count_sum = [0]
for (i, j) in enumerate(operator_count):
    operator_count_sum.append(j + operator_count_sum[-1])
permutation_list = permut(N - 1, N - 1)
answer_max = -(10**9)
answer_min = 10**9
for i in permutation_list:
    answer = A[0]
    for (j, k) in enumerate(i):
        if operator_count_sum[0] <= k < operator_count_sum[1]:
            answer += A[j + 1]
        elif operator_count_sum[1] <= k < operator_count_sum[2]:
            answer -= A[j + 1]
        elif operator_count_sum[2] <= k < operator_count_sum[3]:
            answer *= A[j + 1]
        elif operator_count_sum[3] <= k < operator_count_sum[4]:
            if answer < 0:
                sign = -1
            elif answer > 0:
                sign = 1
            else:
                sign = 0
            answer = abs(answer) // A[j + 1] * sign
    if answer < answer_min:
        answer_min = answer
    if answer > answer_max:
        answer_max = answer
print(answer_max, answer_min, sep="\n")