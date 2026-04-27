from sys import stdin

def input():
    return stdin.readline().strip()

N, Q = map(int, input().split())
A = list(map(int, input().split()))
offset = 0
for _ in range(Q):
    operator, *operand = map(int, input().split())
    if operator == 1:
        index, value = operand
        A[(index - 1 - offset) % N] += value
    elif operator == 2:
        offset += operand[0]
        offset %= N
    elif operator == 3:
        offset -= operand[0]
        offset %= N
A = [A[(i - offset) % N] for i in range(N)]
print(*A)