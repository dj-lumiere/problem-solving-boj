# 11278 2-SAT - 2

from itertools import product

N, M = map(int, input().split())

clauses = []
for _ in range(M):
    i, j = map(int, input().split())
    clauses.append((i, j))
can_be_true = False
for states in product((True, False), repeat=N):
    result = True
    for i, j in clauses:
        sub_result = False
        if i < 0:
            sub_result |= not states[-i - 1]
        else:
            sub_result |= states[i - 1]
        if j < 0:
            sub_result |= not states[-j - 1]
        else:
            sub_result |= states[j - 1]
        result &= sub_result
    if result:
        can_be_true = True
        print(1)
        print(*map(int, states))
        break
else:
    print(0)
