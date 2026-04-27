a = int(input())
m, n = map(int, input().split())
print(min(2*m/a, 2*n/a, max(m,n/a), max(n,m/a), max(m,n)))