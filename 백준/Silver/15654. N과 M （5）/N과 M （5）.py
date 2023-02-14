N, M = list(map(int, input().split(" ")))
num_list = list(map(int, input().split(" ")))
num_list.sort()

def permut(N:int, M:int) -> list[list[int]]:
    list_permut = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            element = []
            for i in stack:
                element.append(num_list[i-1])
            list_permut.append(element)
            return
        else:
            for i in range(1, N+1):
                if i not in stack:
                    stack.append(i)
                    dfs(i+1, M-1, stack)
                    stack.pop()
    dfs(1, M, stack)

    return list_permut

permut_list = permut(N, M)

for i in permut_list:
    print(" ".join(map(str, i)))