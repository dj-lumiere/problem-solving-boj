# 27966 △

N = int(input())
print(N**2 - N - (N - 1))
print(*[f"1 {i}" for i in range(2, N + 1)], sep="\n")