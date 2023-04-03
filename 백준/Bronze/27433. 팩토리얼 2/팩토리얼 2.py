# 27433 팩토리얼 2

N: int = int(input())
def factorial(N: int) -> int:
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)
print(factorial(N))