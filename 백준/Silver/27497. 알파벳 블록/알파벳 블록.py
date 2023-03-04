# D번 - 알파벳 블록

from collections import deque
from sys import stdin

N = int(input())
operation_stack = []
block_assembly = deque()

for i in range(N):
    opcode, *operand = stdin.readline().rstrip().split(" ")
    if opcode == "1":
        block_assembly.append(operand[0])
        operation_stack.append(opcode)
    elif opcode == "2":
        block_assembly.appendleft(operand[0])
        operation_stack.append(opcode)
    elif operation_stack:
        choose_what_letter_to_erase_opcode = operation_stack.pop()
        if choose_what_letter_to_erase_opcode == "1":
            block_assembly.pop()
        else:
            block_assembly.popleft()

if block_assembly:
    print("".join(list(block_assembly)))
else:
    print(0)