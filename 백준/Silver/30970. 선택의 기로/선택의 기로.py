# C번 - 선택의 기로

sort_by_price = [[] for _ in range(10001)]
sort_by_quality = [[] for _ in range(10001)]
N = int(input())
for _ in range(N):
    quality, price = map(int, input().split(" "))
    sort_by_price[price].append(quality)
    sort_by_quality[quality].append(price)
for i in range(10001):
    sort_by_price[i].sort()
    sort_by_quality[i].sort(reverse=True)
select_by_price = []
select_by_quality = []
for i in range(10001):
    if not sort_by_price[i]:
        continue
    select_by_price.append((sort_by_price[i][-1], i))
    sort_by_price[i].pop()
    break
for i in range(10001):
    if not sort_by_price[i]:
        continue
    select_by_price.append((sort_by_price[i][-1], i))
    sort_by_price[i].pop()
    break
for i in range(10000, -1, -1):
    if not sort_by_quality[i]:
        continue
    select_by_quality.append((i, sort_by_quality[i][-1]))
    sort_by_quality[i].pop()
    break
for i in range(10000, -1, -1):
    if not sort_by_quality[i]:
        continue
    select_by_quality.append((i, sort_by_quality[i][-1]))
    sort_by_quality[i].pop()
    break
print(*[" ".join(map(str, i)) for i in select_by_quality])
print(*[" ".join(map(str, i)) for i in select_by_price])
