from collections import deque
import sys

def sol():
    N = int(sys.stdin.readline())
    stack : deque = deque()
    stack_size = 0
    for i in range(N):
        opcode = sys.stdin.readline().rstrip()
        try:
            opcode, operand = opcode.split(" ")
            stack_size += 1
            stack.append(int(operand))
        except:
            if opcode == "pop":
                if stack:
                    sys.stdout.writelines(f"{stack.pop()}\n")
                    stack_size -= 1
                else:
                    sys.stdout.writelines("-1\n")
            elif opcode == "size":
                sys.stdout.writelines(f"{stack_size}\n")
            elif opcode == "empty":
                if not stack:
                    sys.stdout.writelines("1\n")
                else:
                    sys.stdout.writelines("0\n")
            elif opcode == "top":
                if stack:
                    pop_cache = stack.pop()
                    sys.stdout.writelines(f"{pop_cache}\n")
                    stack.append(pop_cache)
                else:
                    sys.stdout.writelines("-1\n")
sol()