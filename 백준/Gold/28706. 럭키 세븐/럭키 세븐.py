# 28706 럭키 세븐

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def is_lucky(available_operations):
    available_mods = [False, True, False, False, False, False, False]
    for (op1, v1), (op2, v2) in available_operations:
        available_mods_sub = [False, False, False, False, False, False, False]
        if op1 == "+":
            for i, v in enumerate(available_mods):
                available_mods_sub[(i + v1) % 7] |= v
        elif op1 == "*":
            for i, v in enumerate(available_mods):
                available_mods_sub[(i * v1) % 7] |= v
        if op2 == "+":
            for i, v in enumerate(available_mods):
                available_mods_sub[(i + v2) % 7] |= v
        elif op2 == "*":
            for i, v in enumerate(available_mods):
                available_mods_sub[(i * v2) % 7] |= v
        available_mods = available_mods_sub[:]
    return available_mods[0]


T = int(input())
for _ in range(T):
    N = int(input())
    available_operations = []
    for _ in range(N):
        op1, v1, op2, v2 = input().split(" ")
        available_operations.append(((op1, int(v1)), (op2, int(v2))))
    result = is_lucky(available_operations)
    if result:
        print("LUCKY\n")
    else:
        print("UNLUCKY\n")