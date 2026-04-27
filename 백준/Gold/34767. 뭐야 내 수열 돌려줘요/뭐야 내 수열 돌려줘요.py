n = int(input())
ps = list(map(int, input().split()))
ps.sort()
pivot = sum(ps)//(n+1)
#print(pivot)
ps_new = [i for i in ps if i != pivot]
#print(ps_new)
p = [0] + ps_new[:n-1] + [pivot]
a = [j-i for i, j in zip(p, p[1:])]
print(*a)