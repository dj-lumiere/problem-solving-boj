n=map(int,input().split())
print(1 if sum(i==1 for i in n) >= 2 else 2)