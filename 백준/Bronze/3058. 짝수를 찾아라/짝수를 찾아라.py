n = int(input())
for _ in range(n):
    m = list(map(int, input().split()))
    print(sum(i for i in m if i%2==0), min(i for i in m if i%2==0))