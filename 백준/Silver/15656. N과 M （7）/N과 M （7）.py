# 15656 N과 M (7)

N, M = list(map(int, input().split(" ")))
num_list = list(map(int, input().split(" ")))
N = len(num_list)
num_list.sort()


def permut(N: int, M: int) -> list[list[int]]:
    list_permut = []
    stack = []

    def dfs(init, M, stack):
        if M == 0:
            element = []
            for i in stack:
                element.append(num_list[i - 1])
            list_permut.append(element)
            return
        else:
            for i in range(1, N+1):
                stack.append(i)
                dfs(i, M-1, stack)
                stack.pop()
    dfs(1, M, stack)

    return list_permut


permut_list = permut(N, M)

for i in permut_list:
    print(*i)