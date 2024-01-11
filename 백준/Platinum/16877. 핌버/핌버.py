# 16877 핌버

from functools import reduce

calculate_max = 3000000
fibs = [1, 2]
grundy_numbers = [0 for _ in range(calculate_max + 1)]
for _ in range(100):
    fibs.append(sum(fibs[-2:]))
    if fibs[-1] > calculate_max:
        fibs.pop()
        break
for i in range(calculate_max + 1):
    next_state = []
    for j in fibs:
        if i < j:
            break
        next_state.append(i - j)
    grundy_next_state = set(map(grundy_numbers.__getitem__, next_state))
    for j in range(16):
        if j not in grundy_next_state:
            grundy_numbers[i] = j
            break
N = int(input())
P = list(map(int, input().split()))
P_grundy_numbers = list(map(grundy_numbers.__getitem__, P))
print("koosaga" if reduce(lambda x, y: x ^ y, P_grundy_numbers) else "cubelover")
