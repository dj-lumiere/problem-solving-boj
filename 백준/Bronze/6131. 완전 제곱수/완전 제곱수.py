from itertools import product

n = int(input())
answer = 0
for a, b in product(range(1, 501), repeat=2):
    if (b <= a and b ** 2 - a ** 2 == -n):
        answer += 1
print(answer)
