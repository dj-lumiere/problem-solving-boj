from itertools import product

p, m, c = map(int, input().split())
x = int(input())
answer = 1000000000000000000000000
for i, j, k in product(range(1, p+1), range(1, m+1), range(1, c+1)):
    answer = min(answer, abs((i+j)*(j+k)-x))
print(answer)