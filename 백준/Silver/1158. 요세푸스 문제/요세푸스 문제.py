N, K = map(int, input().split())
people = list(range(1, N + 1))
deleted = []
index = -1
for i in range(1, N + 1):
    index += K
    index %= (N - i + 1)
    deleted.append(people.pop(index))
    if i == N:
        continue
    index -= 1
    index %= (N - i)
print("<", end="")
print(*deleted, sep=", ", end="")
print(">")
