def sol():
    list_permut = []
    stack = []
    def dfs(init, end, M, stack):
        if M == 0:
            for i in range(init, end+1):
                stack.append(i)
                list_permut.append(sum(j*10**i for i,j in enumerate(stack[::-1])))
                stack.pop()
        else:
            for i in range(init, end+1):
                stack.append(i)
                dfs(0, i-1, M-1, stack)
                stack.pop()

    for i in range(0, 9+1):
        dfs(0, 9, i, stack)

    N = int(input())
    if N >= 1023:
        print(-1)
    else:
        print(list_permut[N])
sol()