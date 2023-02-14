N, M = list(map(int, input().split(" ")))

def permut(N:int, M:int) -> list[list[int]]:
    list_permut = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            return
        else:
            for i in range(init, N+1):
                stack.append(i)
                dfs(i, M-1, stack)
                stack.pop()
    dfs(1, M, stack)

    return list_permut

permut_list = permut(N, M)

for i in permut_list:
    print(" ".join(map(str, i)))