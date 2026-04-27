# 30046 HJS

from itertools import permutations

_ = input()
P = list(input())
Q = list(input())
R = list(input())
for i, j, k in permutations(range(1, 3 + 1), 3):
    substitute = {"H": i, "J": j, "S": k}
    P_substituted = [substitute[l] for l in P]
    Q_substituted = [substitute[l] for l in Q]
    R_substituted = [substitute[l] for l in R]
    if P_substituted < Q_substituted < R_substituted:
        print("HJS! HJS! HJS!")
        break
else:
    print("Hmm...")