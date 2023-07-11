N = int(input())
p = list(map(int, input().split()))
increase_length = [1]
decrease_length = [1]
for i, v in enumerate(p):
    if i == 0:
        continue
    if v > p[i-1]:
        increase_length.append(increase_length[-1]+1)
        decrease_length.append(1)
    elif v == p[i-1]:
        increase_length.append(increase_length[-1])
        decrease_length.append(decrease_length[-1])
    elif v < p[i-1]:
        increase_length.append(1)
        decrease_length.append(decrease_length[-1]+1)
print(max(*increase_length,*decrease_length))