# 2587 대표값2

x = [int(input()) for _ in range(5)]
x.sort()
print(sum(x) // 5, x[2], sep="\n")