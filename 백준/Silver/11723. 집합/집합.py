# 11723 집합

from sys import stdin, stdout

N: int = int(stdin.readline())
user_set: int = 0
all_on: int = (1 << 21) - 1
all_off: int = 0
for i in range(N):
    opcode, *operand_list = stdin.readline().rstrip().split(" ")
    if operand_list:
        operand = int(operand_list[0])
    else:
        operand = 0
    if opcode == "add":
        user_set = user_set | (1 << operand)
    elif opcode == "remove":
        user_set = user_set & (all_on ^ (1 << operand))
    elif opcode == "check":
        stdout.writelines(str((user_set & (1 << operand)) >> operand))
        stdout.writelines("\n")
    elif opcode == "toggle":
        user_set = user_set ^ (1 << operand)
    elif opcode == "all":
        user_set = all_on
    elif opcode == "empty":
        user_set = all_off