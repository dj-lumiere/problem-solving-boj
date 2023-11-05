# 30522 OR & XOR (Small)
from collections import Counter


N, p = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

calculation_list = {}
for k1, v1 in Counter(A).items():
    for k2, v2 in Counter(B).items():
        calculation_list[(k1 ^ k2, k1 | k2)] = (
            calculation_list.get((k1 ^ k2, k1 | k2), 0) + v1 * v2
        )
calculation_list_sorted = sorted(
    calculation_list.items(), key=lambda x: (x[0][1] - x[0][0], x[0][0]), reverse=True
)
result = 0
replaces = 0
for (xored, ored), frequency in calculation_list_sorted:
    if replaces > p:
        result += xored * frequency
    elif replaces + frequency <= p:
        result += ored * frequency
    else:
        result += ored * (p - replaces) + xored * (frequency - (p - replaces))
    replaces += frequency
print(result)
