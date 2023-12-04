# D번 - 피보나치 더하기

from itertools import product

fib = [1, 2]
while fib[-1] <= 10**16:
    fib.append(sum(fib[-2:]))
possible = [set() for _ in range(4)]
for a in range(1, 4):
    for i in product(fib, repeat=a):
        possible[a].add(sum(i))
T = int(input())
for _ in range(T):
    a, b = map(int, input().split(" "))
    print("YES" if b in possible[a] else "NO")