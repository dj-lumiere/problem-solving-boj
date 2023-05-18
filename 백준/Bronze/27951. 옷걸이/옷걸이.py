# A번 - 옷걸이
from collections import Counter

N: int = int(input())
A: list[int] = list(map(int, input().split(" ")))
clothes_count: dict[int, int] = Counter(A)
U, D = map(int, input().split(" "))
if 3 not in clothes_count:
    clothes_count[3] = 0
if clothes_count[1] + clothes_count[3] < U or clothes_count[2] + clothes_count[3] < D:
    print("NO")
else:
    print("YES")
    clothes_list: list[str] = []
    for i in A:
        if i == 1:
            clothes_list.append("U")
            U -= 1
        elif i == 2:
            clothes_list.append("D")
            D -= 1
        elif i == 3 and not U:
            clothes_list.append("D")
            D -= 1
        else:
            clothes_list.append("U")
            U -= 1
    print(*clothes_list, sep="")