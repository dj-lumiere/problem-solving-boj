m, d = int(input()), int(input())
if m==2 and d==18:
    print("Special")
elif m > 2 or (m==2 and d> 18):
    print("After")
else:
    print("Before")