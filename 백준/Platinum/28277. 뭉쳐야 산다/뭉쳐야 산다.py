# 28277 뭉쳐야 산다
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(target: str):
    return stdout.write(target)


def merge_set(a, b):
    result = set()
    adding_set = set()
    if len(S[a]) > len(S[b]):
        result = S[a]
        adding_set = S[b]
    else:
        result = S[b]
        adding_set = S[a]
    for i in adding_set:
        result.add(i)
    S[a] = result
    S[b] = set()


N, Q = map(int, input().split(" "))
S = [set() for _ in range(N + 1)]
for i in range(1, N + 1):
    _, *elements = map(int, input().split(" "))
    S[i] = set(elements)
for _ in range(Q):
    opcode, *operand = map(int, input().split(" "))
    if opcode == 1:
        a, b = operand
        merge_set(a, b)
    if opcode == 2:
        print(f"{len(S[operand[0]])}\n")