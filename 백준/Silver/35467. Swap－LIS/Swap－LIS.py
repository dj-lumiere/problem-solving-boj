n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    if a[i] > a[i+1]:
        print(f"YES\n{i+1} {i+2}")
        break
else:
    print("NO")