# O번

from sys import stdin

Q = int(stdin.readline().strip())
start = 1
end = 1234567890123
step = 1

for _ in range(Q):
    opcode, *operand = list(map(int, stdin.readline().strip().split(" ")))
    if opcode == 0:
        start += operand[0]
        end += operand[0]
    elif opcode == 1:
        start *= operand[0]
        end *= operand[0]
        step *= operand[0]
    elif opcode == 2:
        start += operand[0] * step
    elif opcode == 3:
        print(start)
