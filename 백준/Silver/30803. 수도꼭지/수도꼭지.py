# B번 - 수도꼭지
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
A = [0] + list(map(int, input().split(" ")))
Q = int(input())
toggle = [True] * (N + 1)
current_flow_rate = sum(A)
print(current_flow_rate)
for _ in range(Q):
    operator, *operand = list(map(int, input().split(" ")))
    if operator == 2:
        toggle[operand[0]] ^= True
        if toggle[operand[0]]:
            current_flow_rate += A[operand[0]]
        else:
            current_flow_rate -= A[operand[0]]
    if operator == 1:
        delta = operand[1] - A[operand[0]]
        if toggle[operand[0]]:
            current_flow_rate += delta
        A[operand[0]] = operand[1]
    print(current_flow_rate)