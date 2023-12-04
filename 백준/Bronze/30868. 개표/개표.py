# A번 - 개표

T = int(input())
for _ in range(T):
    N = int(input())
    answer = ["++++"] * (N // 5) + ["|" * (N % 5)]
    print(*answer)