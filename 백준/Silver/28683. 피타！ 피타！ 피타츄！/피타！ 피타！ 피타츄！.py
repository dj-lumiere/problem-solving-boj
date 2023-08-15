# 28683 피타! 피타! 피타츄!
from sys import stdin

def input():
    return stdin.readline().strip()


N = int(input())
if int(N**0.5) ** 2 == N:
    print(-1)
else:
    divisor = []
    possible1 = []
    possible2 = []
    for i in range(1, int(N**0.5) + 1):
        if N % i:
            continue
        divisor.append(i)
    for i in divisor:
        if (i ^ (N // i)) & 1:
            continue
        possible1.append(i)
    for i in range(1, int((N // 2) ** 0.5) + 1):
        if int((N - i**2) ** 0.5) ** 2 == N - i**2:
            possible2.append(i)
    print(len(possible1) + len(possible2))