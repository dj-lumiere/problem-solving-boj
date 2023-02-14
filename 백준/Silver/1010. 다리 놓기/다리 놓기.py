def nCm(n: int, m: int):
    return factorial(n) // (factorial(n-m) * factorial(m))

def factorial(n: int):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

test_cases = int(input())
for i in range(test_cases):
    N, M = list(map(int, input().split(" ")))
    print(nCm(M, N))