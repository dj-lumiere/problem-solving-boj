# 1912 연속합

n: int = int(input())
seq: list[int] = list(map(int, input().split(" ")))
sums: list[int] = [0 for _ in range(n)]
for (i, j) in enumerate(seq):
    if i == 0:
        sums[i] = j
    else:
        if sums[i-1] + j > j:
            sums[i] = sums[i-1] + j
        else:
            sums[i] = j
print(max(sums))