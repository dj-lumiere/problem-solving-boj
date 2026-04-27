# 2554 마지막 팩토리얼 수 2

def last_factorial(N):
    if N < 5:
        return [1, 1, 2, 6, 4][N]
    if N % 5 == 0:
        return pow(2, N // 5, 10) * last_factorial(N // 5) % 10
    if N % 10 >= 6:
        return pow(2, N // 5, 10) * last_factorial(N // 5) * [6, 2, 6, 4][N % 10 - 6] % 10
    return pow(2, N // 5, 10) * last_factorial(N // 5) * [1, 2, 6, 4][N % 10 - 1] % 10

N = int(input())
print(last_factorial(N))