a, b, k, m = map(int, input().split())
possibles = set()
for i in range(10**(k-1), 10**k):
    possible_sub = []
    target = 0
    for j in range(1, (12+k-1)//k+1):
        target *= 10**k
        target += i
        possible_sub.append(target)
        possible_sub.extend([target // (10**x) for x in range(1, len(str(i)))])
    # print(possible_sub)
    for j in possible_sub:
        if a<=j<=b and j >= 10**(k-1):
            possibles.add(j)
sort_possible = sorted(possibles)
answer = 0
for i in sort_possible:
    if i % m:
        continue
    answer += 1
print(answer)