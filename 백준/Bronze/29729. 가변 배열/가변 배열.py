# 29729 가변 배열

S0, N, M = map(int, input().split(" "))
current_size = 0
current_capacity = S0
for _ in range(N + M):
    command = int(input())
    if command == 1:
        current_size += 1
    if command == 0:
        current_size -= 1
    if current_size > current_capacity:
        current_capacity <<= 1
print(current_capacity)
