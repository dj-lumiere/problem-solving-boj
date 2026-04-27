n, k = map(int, input().split())
a = list(map(int, input().split()))
if any(v > k for v in a):
    print(0)
elif any(v <= 0 for v in a):
    print(-1)
else:
    min_flavor = min(a)
    a.pop(a.index(min_flavor))
    print(sum((k-v)//min_flavor for v in a) + 1)