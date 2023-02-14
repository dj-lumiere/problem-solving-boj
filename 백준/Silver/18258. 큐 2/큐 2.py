from collections import deque
import sys

def sol():
    N = int(sys.stdin.readline())
    queue : deque = deque()
    queue_size = 0
    for i in range(N):
        opcode = sys.stdin.readline().rstrip()
        try:
            opcode, operand = opcode.split(" ")
            queue_size += 1
            queue.appendleft(int(operand))
        except:
            if opcode == "pop":
                if queue:
                    sys.stdout.writelines(f"{queue.pop()}\n")
                    queue_size -= 1
                else:
                    sys.stdout.writelines("-1\n")
            elif opcode == "size":
                sys.stdout.writelines(f"{queue_size}\n")
            elif opcode == "empty":
                if not queue:
                    sys.stdout.writelines("1\n")
                else:
                    sys.stdout.writelines("0\n")
            elif opcode == "front":
                if queue:
                    pop_cache = queue.pop()
                    sys.stdout.writelines(f"{pop_cache}\n")
                    queue.append(pop_cache)
                else:
                    sys.stdout.writelines("-1\n")
            elif opcode == "back":
                if queue:
                    pop_cache = queue.popleft()
                    sys.stdout.writelines(f"{pop_cache}\n")
                    queue.appendleft(pop_cache)
                else:
                    sys.stdout.writelines("-1\n")
sol()