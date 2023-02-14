# C번 - 수학 퀴즈

N = int(input())
A = list(map(int, input().split(" ")))

p, q = 0, 0

for i in A:
    if i % 3 == 0:
        q += 1
    elif i % 3 == 1:
        p += 1
    else:
        p -= 1
        q -= 1

print(p, q)