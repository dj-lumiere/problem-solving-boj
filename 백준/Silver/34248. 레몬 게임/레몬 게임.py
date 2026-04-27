n = int(input())
a = list(map(int, input().split()))
if all(i==2 for i in a):
    print("No")
elif sum(a) % 3 != 0:
    print("No")
else:
    print("Yes")