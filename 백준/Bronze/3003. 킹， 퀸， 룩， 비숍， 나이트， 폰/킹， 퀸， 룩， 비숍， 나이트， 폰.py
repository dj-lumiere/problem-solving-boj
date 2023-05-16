# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰

A = list(map(int, input().split(" ")))
pieces = [1, 1, 2, 2, 2, 8]
print(" ".join(map(str, [j - i for i, j in zip(A, pieces)])))