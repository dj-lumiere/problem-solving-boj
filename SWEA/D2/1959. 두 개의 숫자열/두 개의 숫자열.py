from itertools import product
t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n > m:
        a, b = b, a
        n, m = m, n
    results = [0 for _ in range(n+m)]
    for (i1, v1), (i2, v2) in product(enumerate(a), enumerate(reversed(b))):
         results[i1+i2] += v1*v2
    print(f"#{i} {max(results[n-1:m])}")