# 1182 부분수열의 합

# 원소 갯수별로 슬라이딩 윈도우

N, S = list(map(int, input().split(" ")))
integer_list = list(map(int, input().split(" ")))
global answer
answer = 0


def permut(N: int, M: int) -> list[list[int]]:
    list_permut = []
    stack = []

    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            if sum(
                [integer_list[i] for (i, j) in enumerate(stack) if j == 1]
            ) == S and sum(stack):
                global answer
                answer += 1
            return
        else:
            # 중복순열
            for i in range(0, N):
                stack.append(i)
                dfs(i, M - 1, stack)
                stack.pop()

    dfs(0, M, stack)

    return list_permut


permut(2, N)
print(answer)