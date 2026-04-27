n, m=map(int, input().split())
answer=0
keys = []
for i in range(1, m+1):
    c, p = map(int, input().split())
    keys.extend([(c,i),(p,i)])
keys.sort(key=lambda x:x[0])
print(keys[(n-1)%(2*m)][1])