n, k = map(int, input().split())
s = list(input())
rain_days = [sum(i=="L" for i in s[:k])]
for i, (v1, v2) in enumerate(zip(s, s[k:])):
     rain_days.append(rain_days[-1]-(v1=="L")+(v2=="L"))
print(rain_days.index(max(rain_days))+1)