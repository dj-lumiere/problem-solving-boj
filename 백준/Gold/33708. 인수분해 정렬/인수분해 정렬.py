n = int(input())
a = list(map(int, input().split()))
already_sorted = a == sorted(a)
any_composite = any(any(v%v2==0 for v2 in range(2, int(v**.5)+1))for v in a)
if already_sorted:
    print("YES")
elif any_composite:
    print("YES")
elif len(set(a)) >= 2 and any(v!=1 and v2!=1 for v,v2 in zip(a, a[1:])):
    print("YES")
else:
    print("NO")