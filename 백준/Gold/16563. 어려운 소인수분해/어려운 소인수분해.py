from sys import stdin, stdout

N = int(input())
k = list(map(int, stdin.readline().rstrip().split(" ")))

# 소인수 분해 후
finder_limit = int(5000000**0.5) + 1
prime_list: list[bool] = [False]*2+[True for i in range(0, finder_limit + 1)]
for x in range(1, int(finder_limit**0.5) + 1):
    if prime_list[x]:
        prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
        prime_list[x] = True
prime_list2 = [i for i, j in enumerate(prime_list) if j]

for i in k:
    next_factor = i
    for j in prime_list2:
        while next_factor % j == 0:
            print(j, end=" ")
            next_factor = next_factor // j
    if next_factor != 1:
        print(next_factor)
    else:
        print()