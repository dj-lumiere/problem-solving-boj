n = int(input())
a = list(map(int, input().split()))
for i in range(1, n//2+1):
    if a[:i] == a[n-i:]:
        print("yes")
        break
else:
    print("no")