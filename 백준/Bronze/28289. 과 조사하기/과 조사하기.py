# 28289 과 조사하기

P = int(input())
sector_count = [0, 0, 0, 0, 0]
for _ in range(P):
    g, c, _ = map(int, input().split(" "))
    if g == 1:
        sector_count[4] += 1
    elif c in [1, 2]:
        sector_count[1] += 1
    elif c == 3:
        sector_count[2] += 1
    elif c == 4:
        sector_count[3] += 1
print(*sector_count[1:], sep="\n")