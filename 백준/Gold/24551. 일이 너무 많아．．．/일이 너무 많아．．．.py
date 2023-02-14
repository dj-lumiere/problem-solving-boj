# 24551 일이 너무 많아...

from itertools import product

N = int(input())
result = 0

def permut(N:int, M:int) -> list[list[int]]:
    list_permut = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            return
        else:
            #조합
            for i in range(init, N+1):
                stack.append(i)
                dfs(i+1, M-1, stack)
                stack.pop()
    dfs(0, M, stack)
    return list_permut

prime_under18 = [2, 3, 5, 7, 11, 13, 17]
factors_initial = [(10**i - 1) // 9 for i in prime_under18]
factors = [[] for i in range(7)]
for i in range(7):
    if i == 0:
        for j in factors_initial:
            if j <= N:
                factors[0].append(j)
    else:
        list_permut = permut(6, i + 1)
        for j in list_permut:
            item_sub = 1
            for k in j:
                item_sub *= factors_initial[k]
            if item_sub <= N:
                factors[i].append(item_sub)
for i in range(7):
    for j in factors[i]:
        result += N // j * (-1) ** i
print(result)